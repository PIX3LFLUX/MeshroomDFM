# instructions for creating new nodes: https://github.com/natowi/meshroom_external_plugins/wiki/2-DevDoc
# has to be exported to pyc file, then placed into /lib/meshroom/nodes/aliceVision

# from meshroom.core import desc
import json
from meshroom.core import desc


# command line node, calls another program through the command line
class DFMImageTree(desc.Node):

    inputs = [
        desc.File(
                name="sfmData",
                label="SfMData",
                description="SFM data file.",
                value=desc.Node.internalFolder,
                uid=[0],
		),
    ]

    outputs = [
        desc.File(
            name="ImagePairs",
            label="Image Pairs",
            description="Path to a file which contains the list of image pairs to match.",
            value=desc.Node.internalFolder + "imageMatches.txt",
            uid=[0],
		)
    ]

    def create_image_pairs(self, imagePairsFile, sfmFile, chunk):
        """
        Loads imagePairsFile and creates an array of image pairs to run dfm on.
        """
        chunk.logger.info(f"sfm File: {sfmFile}")
        with open(sfmFile, 'r', encoding='utf-8', errors='ignore') as f:
            sfmData = json.load(f)

        imageIds = []
        chunk.logger.info('this is an info log2')

        chunk.logger.info(f" created the following imageIds: {imageIds}")

        for imageData in sfmData["views"]:
            imageIds.append(imageData["viewId"])

        chunk.logger.info(f" created the following imageIds: {imageIds}")

        with open(imagePairsFile, 'w', encoding='utf-8', errors='ignore') as f:
            for idx, imageId in enumerate(imageIds):
                line = ' '.join(imageIds[idx:])
                f.write(line)
                f.write('\n')

    def processChunk(self, chunk):
        try:
            chunk.logManager.start('debug')
            chunk.logger.info('this is an info log')

            self.create_image_pairs(chunk.node.ImagePairs.value, chunk.node.sfmData.value, chunk)

        except Exception as e:
            chunk.logger.error(e)
            raise RuntimeError()
        finally:
            # required to unlock log file so that it can be deleted if required
            chunk.logManager.end()

        

