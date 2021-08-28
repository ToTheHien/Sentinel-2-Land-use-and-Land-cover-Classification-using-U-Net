#!/bin/bash

# Create text file to contain the list of data

# Change to directory that contain the original Sentinel-2 dataset
cd /media/thehien/Endo/RGB/Original

# Create a text file data.txt and list all the file name in 'Original' folder
# Collect all the dataset name to a text file
# This list will contain the text file, therefore you need to remove the first line in the text file before using it
ls -A > data.txt

# Move the previous text file to a main folder
mv data.txt /media/thehien/Endo/RGB
