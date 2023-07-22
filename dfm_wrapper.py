import json
from utils.DeepFeatureMatcher import DeepFeatureMatcher
import numpy as np
from PIL import Image
import os
import csv
import argparse

def main(sfmDataFile, imagePairsFile, matchesFolder, featuresFolder, minMatches):

    imagePairs = load_image_pairs(imagePairsFile, sfmDataFile)
    dfm(imagePairs, matchesFolder, featuresFolder, minMatches)

def load_image_pairs(imagePairsFile, sfmFile):
    """
    Loads imagePairsFile and creates an array of image pairs to run dfm on.
    """
    with open(sfmFile, 'r', encoding='utf-8', errors='ignore') as f:
        sfmData = json.load(f)

    with open(imagePairsFile, 'r', encoding='utf-8', errors='ignore') as f:
        imageTree = [row[0].split(' ') for row in csv.reader(f, delimiter='\n')]

    imagePairs = []
    for row in imageTree:
        image1 = row[0]
        for image in row[1:]:
            image2 = image

            image1Data = next(item for item in sfmData["views"] if str(item["viewId"]) == image1)
            image2Data = next(item for item in sfmData["views"] if str(item["viewId"]) == image2)

            imagePairs.append([image1Data, image2Data])

    return imagePairs

            

def dfm(imagePairs, matchesFolder, featuresFolder, minMatches):
    """
    Runs dfm algorithm on imagePairs.
    Returns the matches of each image Pair.
    """

    if not os.path.exists(matchesFolder):
        os.makedirs(matchesFolder)

    if not os.path.exists(featuresFolder):
        os.makedirs(featuresFolder)

    fm = DeepFeatureMatcher(enable_two_stage=True, model='VGG19_BN', ratio_th=[0.9, 0.9, 0.9, 0.9, 0.95, 1.0], bidirectional=True)

    # create a dictonary containing the offsets for every image id
    imageIdList1 = [str(id[0]["viewId"]) for id in imagePairs]
    imageIdList2 = [str(id[1]["viewId"]) for id in imagePairs]
    imageIdList = imageIdList1 + imageIdList2
    offsets = dict.fromkeys(imageIdList, 0)

    num_pairs = int(len(imageIdList)/2)
    log_percent = 1
    log_every = num_pairs*log_percent/100
    log_idx = 0

    # match the image pairs
    for idx, imagePair in enumerate(imagePairs):
        image1Path = imagePair[0]["path"]
        image2Path = imagePair[1]["path"]
        image1Id = str(imagePair[0]["viewId"])
        image2Id = str(imagePair[1]["viewId"])

        imageA = np.array(Image.open(image1Path))
        imageB = np.array(Image.open(image2Path))

        H, H_init, points_A, points_B = fm.match(imageA, imageB)

        keypoints0 = points_A.T
        keypoints1 = points_B.T

        # create matches array
        # TODO: since every detected feature is a match, this is redundant. Remove this and write the offset for the matches directly
        mtchs = np.vstack([np.arange(0, keypoints0.shape[0])]*2).T

        if len(mtchs) >= minMatches:
            # write matches file (matches keypoints from imgA to keypoints from imgB) 
            with open(os.path.join(matchesFolder, f"{idx}.matches.txt"), 'a') as f:
                f.write(f"{image1Id} {image2Id}\n")
                f.write("1\n")
                f.write(f"dspsift {len(mtchs)}\n")
                for match in mtchs:
                    f.write(f"{match[0] + offsets[image1Id]} {match[1] + offsets[image2Id]}\n")

            # # write features to file
            with open(os.path.join(featuresFolder, str(image1Id + ".dspsift.feat")), 'a') as f:
                for keypoint in keypoints0:
                    f.write(' '.join(str(item) for item in keypoint) + '\n')

            with open(os.path.join(featuresFolder, str(image2Id + ".dspsift.feat")), 'a') as f:
                for keypoint in keypoints1:
                    f.write(' '.join(str(item) for item in keypoint) + '\n')

            # increment offset dict
            offsets[image1Id] += len(mtchs)
            offsets[image2Id] += len(mtchs)

            if idx+1 >= log_every*log_idx:
                print(f"{idx+1}/{num_pairs} pairs matched")
                log_idx += 1

        else:
            print(f"Not enough matches for pair {image1Id}, {image2Id}: {len(mtchs)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sfmData', type=str, required=True)
    parser.add_argument('-imagePairs', type=str, required=True)
    parser.add_argument('-matches', type=str, required=True)
    parser.add_argument('-features', type=str, required=True)
    parser.add_argument('--minMatches', type=int)

    args = parser.parse_args()

    print(f"""Executing the deep feature matching alforithm with the following parameters:
    sfmData: {args.sfmData}
    imagePairs: {args.imagePairs}
    matches: {args.matches}
    features: {args.features}
    minMatches: {args.minMatches}""")

    main(args.sfmData, args.imagePairs, args.matches, args.features, args.minMatches)