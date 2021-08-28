#!/bin/bash
#This script filters every 10 meter resolution image including band 2, 3 and 4
#usage: ./filter.sh

# Change directory to the main folder in order to read 'data.txt'
cd /media/thehien/Endo/RGB/
filename='data.txt'
while read data
do
	cd /media/thehien/Endo/RGB/Original/$data/
	# Create a new folder to contain all the 10 meter resolution images
	mkdir /media/thehien/Endo/RGB/10m/$data/
	i=1
	for kep in *.jp2
	do
    		case $i in 
    		2)
    			mv $kep /media/thehien/Endo/RGB/10m/$data/
    			;;
    		3)
    			mv $kep /media/thehien/Endo/RGB/10m/$data/
    			;;
    		4)
    			mv $kep /media/thehien/Endo/RGB/10m/$data/
    			break
    			;;
    		esac
    	
    		i=$((i+1))
	done

done < $filename


