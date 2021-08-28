#!/bin/bash
#This script performs a layer stack of all .tif images inside the folder
#usage: ./merge.sh
##############################################

# Working with each data set
cd /media/thehien/Endo/RGB/
filename='data.txt'
while read data
do
	cd /media/thehien/Endo/RGB/Clip/$data/
	output=`ls *.tif| head -n 1 | awk -F "_" '{print $3}'`
	output+='.tif'
	echo $output
	echo ""
	echo "<----------------------------------------"
	sds_names=""

	for kep in *.tif
	do    
    		echo "$(basename "$kep")"
    		sds=$(echo "$(basename "$kep")")
    		sds_names="$sds $sds_names"
	done


	# Create the stack
	gdal_merge.py -n -9999 -a_nodata -9999 -separate -o $output $sds_names 
	# Move output to Stacked directory
	mv $output /media/thehien/Endo/RGB/Merge/

done < $filename
