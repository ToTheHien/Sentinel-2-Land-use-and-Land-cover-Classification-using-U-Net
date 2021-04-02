#!/bin/bash
#This script performs a layer stack of all .tif images inside the folder
#usage: ./merge.sh
##############################################

# Working with each data set
cd /media/thehien/Endo/Sentinel-2A/
filename='data.txt'
while read data
do
	cd /media/thehien/Endo/Sentinel-2A/Resample_10m/$data/
	output=`ls *.tif| head -n 1 | awk -F "_B" '{print $1}'`
	output+='_stacked.tif'
	echo $output
	echo ""
	echo "<----------------------------------------"
	sds_names=""

	for kep in *.tif
	do    
    		echo "$(basename "$kep")"
    		sds=$(echo "$(basename "$kep")")
    		sds_names="$sds_names $sds"
	done

	echo ""
	echo "<----------------------------------------"
	echo "All bandnames:"
	echo $sds_names

	# Create the stack
	gdal_merge.py -n -9999 -a_nodata -9999 -separate -of GTiff -o $output $sds_names 
	# Query the new stack for metadata
	gdalinfo $output
	# Move output to Stacked directory
	mv *_stacked* /media/thehien/Endo/Sentinel-2A/Stacked/

done < $filename
