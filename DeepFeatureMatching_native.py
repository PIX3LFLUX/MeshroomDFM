# instructions for creating new nodes: https://github.com/natowi/meshroom_external_plugins/wiki/2-DevDoc
# has to be exported to pyc file, then placed into /lib/meshroom/nodes/aliceVision

# from meshroom.core import desc
import json
from utils.DeepFeatureMatcher import DeepFeatureMatcher
import numpy as np
from PIL import Image
import os
import csv
from meshroom.core import desc


# command line node, calls another program through the command line
class DeepFeatureMatching(desc.Node):

    inputs = [
        desc.File(
                name="sfmDataIn",
                label="SfMData",
                description="SFM data file.",
                value=desc.Node.internalFolder,
                uid=[0],
		),
        desc.File(
                name="ImagePairs",
                label="Image Pairs",
                description="Path to a file which contains the list of image pairs to match.",
                value=desc.Node.internalFolder,
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="matches",
            label="Matches Folder",
            description="Matched features file",
            value=desc.Node.internalFolder,
            uid=[0],
            )
    ]

    def load_image_pairs(self, imagePairsFile, sfmFile):
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

                

    def dfm(self, imagePairs, matchesFolder):
        """
        Runs dfm algorithm on imagePairs.
        Returns the matches of each image Pair.
        """

        if not os.path.exists(matchesFolder):
            os.makedirs(matchesFolder)

        fm = DeepFeatureMatcher(enable_two_stage=True, model='VGG19_BN', ratio_th=[0.9, 0.9, 0.9, 0.9, 0.95, 1.0], bidirectional=True)
        torch.cuda.empty_cache()
        # print(torch.cuda.memory_summary(device=None, abbreviated=False))

        # create a dictonary containing the offsets for every image id
        imageIdList1 = [str(id[0]["viewId"]) for id in imagePairs]
        imageIdList2 = [str(id[1]["viewId"]) for id in imagePairs]
        imageIdList = imageIdList1 + imageIdList2
        offsets = dict.fromkeys(imageIdList, 0)

        # match the image pairs
        for imagePair in imagePairs:
            if self.stopped:
                print("User pressed stop button, exiting dfm!")
                break
            
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

            # old, saves keypoints and matches to npz file
            # matchesFileName = str(imagePair[0]["viewId"]) + '_' + str(imagePair[1]["viewId"]) + "_matches"
            # np.savez_compressed(os.path.join(matchesFolder, matchesFileName),
            #                     keypoints0=keypoints0,
            #                     keypoints1=keypoints1,
            #                     matches=mtchs)

            
            

            # PROBLEM: dfm program doesn't search for all features, instead it matches features from two images
            # SOLUTION: do feature matching with dfm, append all features of one image to a file


            # write matches file (matches keypoints from imgA to keypoints from imgB) 
            with open(os.path.join(matchesFolder, "matches.txt"), 'a') as f:
                f.write(f"{image1Id} {image2Id}\n")
                f.write("1\n")
                f.write(f"dspsift {len(mtchs)}\n")
                for match in mtchs:
                    f.write(f"{match[0] + offsets[image1Id]} {match[1] + offsets[image2Id]}\n")

            # # write features to file
            with open(os.path.join(matchesFolder, str(image1Id + ".feat")), 'a') as f:
                for keypoint in keypoints0:
                    f.write(' '.join(str(item) for item in keypoint) + '\n')

            with open(os.path.join(matchesFolder, str(image2Id + ".feat")), 'a') as f:
                for keypoint in keypoints1:
                    f.write(' '.join(str(item) for item in keypoint) + '\n')

            # increment offset dict
            offsets[image1Id] += len(mtchs)
            offsets[image2Id] += len(mtchs)

    def processChunk(self, chunk):
        # code for the node to run goes here
        self.stopped = False
        imagePairs = self.load_image_pairs(self.inputs[1], self.inputs[0])
        self.dfm(imagePairs, self.outputs[0])

    # optional
    def stopProcess(self, chunk):
        # code here runs when the stop button is clicked
        self.stopped = True


# for testing
# if __name__ == "__main__":
#     dfm = DeepFeatureMatching()
    
#     imagePairs = dfm.load_image_pairs("MeshroomCache/ImageMatching/7a9949f2e5fa37a71e1895aa17c45a4af092827f/imageMatches.txt",
#                                       "MeshroomCache/CameraInit/2cea201c6f73eb7fede71e3a7c333d82b58b2381/viewpoints.sfm")

#     dfm.dfm(imagePairs, "matches")