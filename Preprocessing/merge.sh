#!/bin/bash
#This script performs a layer stack of all .tif images inside the folder
#usage: ./merge.sh
##############################################

output=`ls *.jp2| head -n 1 | awk -F "_B" '{print $1}'`
output+='_stacked.tif'
echo $output
echo ""
echo "<----------------------------------------"
sds_names=""

for kep in *.jp2;do # You can change the file extension with any valid file extension
    echo "$(basename "$kep")"
    sds=$(echo "$(basename "$kep")")
    sds_names="$sds_names $sds"
done

echo ""
echo "<----------------------------------------"
echo "All bandnames:"
echo $sds_names

# Create the stack
gdal_merge.py -n -9999 -a_nodata -9999 -separate -of HFA -o $output $sds_names 
# Query the new stack for metadata
gdalinfo $output
