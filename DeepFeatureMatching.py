# instructions for creating new nodes: https://github.com/natowi/meshroom_external_plugins/wiki/2-DevDoc
# has to be exported to pyc file, then placed into /lib/meshroom/nodes/aliceVision

from meshroom.core import desc

# command line node, calls another program through the command line
class DeepFeatureMatching(desc.CommandLineNode):
    # command = 'dfm_wrapper {allParams}'
    commandLine = 'dfm_wrapper -sfmData {sfmDataValue} -imagePairs {imagePairsValue} -matches {matchesValue} -features {featuresValue} --minMatches {minMatchesValue}'

    inputs = [
        desc.File(
                name="sfmData",
                label="SfMData",
                description="SFM data file.",
                value=desc.Node.internalFolder,
                uid=[0],
		),
        desc.File(
                name="imagePairs",
                label="Image Pairs",
                description="Path to a file which contains the list of image pairs to match.",
                value=desc.Node.internalFolder,
                uid=[0],
		),
        desc.IntParam(
            name='minMatches',
            label='Minimum Matches',
            description='''The minimum number of matches required in order to save image pair in matches file''',
            value=100,
            range=None,
            uid=[0],
        )
    ]

    outputs = [
        desc.File(
            name="matches",
            label="Matches Folder",
            description="Matched features file",
            value=desc.Node.internalFolder + '/matches',
            uid=[0],
            ),
        desc.File(
        name="features",
        label="Features Folder",
        description="Output path for the features files (*.feat)",
        value=desc.Node.internalFolder + '/features',
        uid=[0],
        )
    ]