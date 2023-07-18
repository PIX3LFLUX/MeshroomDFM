# instructions for creating new nodes: https://github.com/natowi/meshroom_external_plugins/wiki/2-DevDoc
# has to be exported to pyc file, then placed into /lib/meshroom/nodes/aliceVision

from meshroom.core import desc

# command line node, calls another program through the command line
class DeepFeatureMatchingAnalyzer(desc.CommandLineNode):
    # command = 'dfm_wrapper {allParams}'
    commandLine = 'dfm_analyzer -sfmData {sfmDataValue} -matches {matchesValue} -features {featuresValue} -output {outputValue}'

    inputs = [
        desc.File(
                name="sfmData",
                label="SfMData",
                description="SFM data file.",
                value=desc.Node.internalFolder,
                uid=[0],
		),
        desc.File(
            name="matches",
            label="Matches Folder",
            description="Matched features file",
            value=desc.Node.internalFolder,
            uid=[0],
            ),
        desc.File(
            name="features",
            label="Features Folder",
            description="Input path for the features files (*.feat)",
            value=desc.Node.internalFolder,
            uid=[0]
        )
    ]

    outputs = [
        desc.File(
        name="output",
        label="Image output Folder",
        description="Output path for the images",
        value=desc.Node.internalFolder + "/matched_images",
        uid=[0],
        )
    ]