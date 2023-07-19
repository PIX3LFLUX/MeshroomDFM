#!/bin/bash

VERSION="v1.0.0"

# Concatenate the split files into a temporary ZIP file
cat "MeshroomDFM-$VERSION"* > "temp.zip"

# Check if unzip is installed
if ! command -v unzip &> /dev/null; then
  echo "Error: unzip command not found. Please install unzip to extract the content of the ZIP file."
  exit 1
fi

# Extract the content of the ZIP file
unzip "temp.zip"

# Clean up
rm "temp.zip"
rm -rf upload
rm "MeshroomDFM-$VERSION"*
rm install.sh

echo "Unzipped the binaries"
