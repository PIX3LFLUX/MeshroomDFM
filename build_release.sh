#!/bin/bash

VERSION="v1.0.0"
INCLUDE_FILES="DeepFeatureMatching.py DeepFeatureMatchingAnalyzer.py DFMImageTree.py"

# Create the directories
mkdir -p releases
mkdir -p "releases/$VERSION"
mkdir -p "releases/$VERSION/upload"

# Copy the binaries
cp dist/* releases/$VERSION

# Copy the include files
for filename in $INCLUDE_FILES; do
    cp "$filename" "releases/$VERSION/$filename"
done

# Create zip file
cd releases/$VERSION || exit 1
zip -r "temp.zip" *

# Split the temporary archive into files of size 1900M
split -b 1900M "temp.zip" "upload/MeshroomDFM-$VERSION"

cd ../..

# copy the install script
cp install.sh "releases/$VERSION/upload"

echo "Release preparation for version $VERSION complete."