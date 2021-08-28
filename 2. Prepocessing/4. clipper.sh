#!/bin/bash
#This script crops every image inside the folder with a specific based on a vector file, by using GDAL, and moves the cropped images to a specific folder location
#usage: ./clipper.sh


cd /media/thehien/Endo/RGB/
filename='data.txt'
while read data
do
	cd /media/thehien/Endo/RGB/10m/$data/
	# Create a new folder that contain all the clipped images
	mkdir /media/thehien/Endo/RGB/Clip/$data/
	# Clipping 
	for kep in *.jp2
	do
    		echo "$(basename "$kep")"
    		gdalwarp -q -cutline /media/thehien/Endo/Dalat/Dalat.shp -to SRC_METHOD=GEOTRANSFORM -to DST_METHOD=GEOTRANSFORM -t_srs '+proj=utm +zone=48N +datum=WGS84' -crop_to_cutline -tr 10.0 10.0 -of GTiff  $kep ${kep/.jp2}_clipped.tif
    		mv *_clipped* /media/thehien/Endo/RGB/Clip/$data/
	done

done < $filename


