#!/bin/bash
#This script crops every image inside the folder with a specific based on a vector file, by using GDAL, and moves the cropped images to a specific folder location
#usage: ./clipper.sh
echo ""
echo "<----------------------------------------"
echo "Start Clipper"
for kep in *_stacked.tif;do # You can change the file extension with any valid file extension
    echo "$(basename "$kep")"
    gdalwarp -q -cutline /media/thehien/Endo/DaLat/DaLat.shp -crop_to_cutline -tr 10.0 10.0 -of GTiff  $kep ${kep/.tif}_cropped.tif;done

echo ""
echo "<----------------------------------------"
echo "Start Moving files"
mv *_stacked_cropped* /media/thehien/Endo/Sentinel-2A/Clipper/
