import csv
import json
import os
import cv2
import numpy as np
from PIL import Image
import argparse

def main(matchesFolder, featuresFolder, sfmDataFile, outputDir):

    # Create output directory and load the input data
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    with open(sfmDataFile, 'r', encoding='utf-8', errors='ignore') as f:
        sfmData = json.load(f)

    matchesFiles = os.listdir(matchesFolder)

    # Iterate over all matches.txt files
    for matchesFile in matchesFiles:
        with open(os.path.join(matchesFolder, matchesFile), 'r') as f:
            lines = f.read().splitlines()

        imageA = lines[0].split(" ")[0]
        imageB = lines[0].split(" ")[1]

        with open(os.path.join(featuresFolder, imageA + ".dspsift.feat"), 'r') as f:
            featuresA = f.read().splitlines()

        with open(os.path.join(featuresFolder, imageB + ".dspsift.feat"), 'r') as f:
            featuresB = f.read().splitlines()

        # load matching features between imageA and imageB, save coordinates in matches list
        matches = [[], []]
        for line in lines[3:]:
            match_posA = int(line.split(" ")[0])
            match_posB = int(line.split(" ")[1])
            matchA = list(map(float, featuresA[match_posA].split(" ")))
            matchB = list(map(float, featuresB[match_posB].split(" ")))

            matches[0].append(matchA)
            matches[1].append(matchB)

        # get the image path from viedId
        imgPath_A = next(item["path"] for item in sfmData["views"] if str(item["viewId"]) == imageA)
        imgPath_B = next(item["path"] for item in sfmData["views"] if str(item["viewId"]) == imageB)

        # load the images
        img_A = np.array(Image.open(imgPath_A))
        img_B = np.array(Image.open(imgPath_B))

        # draw and save the matches
        result_img = draw_matches(img_A, img_B, matches[0], matches[1])
        cv2.imwrite(os.path.join(outputDir, imageA + "_" + imageB + ".png"), result_img)


def draw_matches(img_A, img_B, keypoints0, keypoints1):
    """Arranges img_A and img_B horizontally and draws lines between matched features"""
    
    p1s = []
    p2s = []
    dmatches = []
    for i, (x1, y1) in enumerate(keypoints0):
         
        p1s.append(cv2.KeyPoint(x1, y1, 1))
        p2s.append(cv2.KeyPoint(keypoints1[i][0], keypoints1[i][1], 1))
        j = len(p1s) - 1
        dmatches.append(cv2.DMatch(j, j, 1))
        
    matched_images = cv2.drawMatches(cv2.cvtColor(img_A, cv2.COLOR_RGB2BGR), p1s, 
                                     cv2.cvtColor(img_B, cv2.COLOR_RGB2BGR), p2s, dmatches, None)
    
    return matched_images


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sfmData', type=str, required=True)
    parser.add_argument('-matches', type=str, required=True)
    parser.add_argument('-features', type=str, required=True)
    parser.add_argument('-output', type=str, required=True)

    args = parser.parse_args()
    main(args.matches, args.features, args.sfmData, args.output)