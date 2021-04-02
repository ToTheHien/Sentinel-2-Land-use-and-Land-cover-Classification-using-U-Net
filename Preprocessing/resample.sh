#!/bin/bash
#This script performs resampling of the bands with 20 m to 10m resolution using a bilinear method, by using GDAL
#Place this script inside the folder of the Sentinel-2 bands with 20m resolution
#usage: ./resample.sh

cd /media/thehien/Endo/Sentinel-2A/
filename='data.txt'
while read data
do
	cd /media/thehien/Endo/Sentinel-2A/Original/$data/
	mkdir /media/thehien/Endo/Sentinel-2A/Resample_10m/$data/
	# Resampling 
	for kep in *.jp2
	do
    		gdalwarp -overwrite -s_srs EPSG:32634 -t_srs EPSG:32634 -r bilinear -ts 10980 10980 -of GTiff $kep ${kep/.jp2}_10m.tif
    		mv *_10m* /media/thehien/Endo/Sentinel-2A/Resample_10m/$data/
	done

done < $filename
