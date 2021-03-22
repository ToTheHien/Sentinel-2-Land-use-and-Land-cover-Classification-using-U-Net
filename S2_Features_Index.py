#!/usr/bin/env python
# coding: utf-8

# In[20]:


import glob
import numpy as np
from osgeo import gdal # If GDAL doesn't recognize jp2 format, check version


# In[21]:


# Set input directory
in_dir = '/media/thehien/Endo/Sentinel-2A/L2A_T48PZU_A010254_20190222T031329_2019-02-22/'


# In[22]:


# Search directory for desired bands
blue_file  = glob.glob(in_dir + '**B02.jp2') # blue band
green_file = glob.glob(in_dir + '**B03.jp2') # green band
red_file   = glob.glob(in_dir + '**B04.jp2') # red band
nir_file   = glob.glob(in_dir + '**B08.jp2') # nir band


# In[23]:


# Define a function to calculate NDVI using band arrays for red, NIR bands
def ndvi(red, nir):
    return ((nir - red)/(nir + red))


# In[24]:


# Define a function to calculate NDRE using band arrays for red edge, NIR bands
def ndwi(green, nir):
    return ((green - nir)/(green + nir))


# In[25]:


# Define a function to calculate EVI using band arrays for blue, red, NIR bands
def evi(blue, red, nir):
    return (2.5*(nir - red)/(nir + 6*red - 7.5*blue + 1))


# In[26]:


# Define a function to calculate SAVI using band arrays for red, NIR bands
def savi(red, nir):
    return ((1 + 0.5)*(nir - red)/(nir + red + 0.5))


# In[27]:


# Open each band using gdal
blue_link  = gdal.Open(blue_file[0])
green_link = gdal.Open(green_file[0])
red_link   = gdal.Open(red_file[0])
nir_link   = gdal.Open(nir_file[0])


# In[28]:


# read in each band as array and convert to float for calculations
blue  = blue_link.ReadAsArray().astype(np.float)
green = green_link.ReadAsArray().astype(np.float)
red   = red_link.ReadAsArray().astype(np.float)
nir   = nir_link.ReadAsArray().astype(np.float)


# In[29]:


# Call the ndvi() function on red, NIR bands
ndvi2 = ndvi(red, nir)
# Call the ndwi() function on green, NIR bands
ndwi2 = ndwi(green, nir)
# Call the evi()  function on blue, red, NIR bands
evi2  = evi(blue, red, nir)
# Call the savi() function on red, NIR bands
savi2 = savi(red, nir)


# In[30]:


# Create output filename based on input name 
outfile_name_ndvi = red_file[0].split('_B')[0] + '_NDVI.tif'
outfile_name_ndwi = red_file[0].split('_B')[0] + '_NDWI.tif'
outfile_name_evi  = red_file[0].split('_B')[0] + '_EVI.tif'
outfile_name_savi = red_file[0].split('_B')[0] + '_SAVI.tif'


# In[31]:


x_pixels_ndvi = ndvi2.shape[0]  # number of pixels in x
y_pixels_ndvi = ndvi2.shape[1]  # number of pixels in y

x_pixels_ndwi = ndwi2.shape[0]  # number of pixels in x
y_pixels_ndwi = ndwi2.shape[1]  # number of pixels in y

x_pixels_evi = evi2.shape[0]  # number of pixels in x
y_pixels_evi = evi2.shape[1]  # number of pixels in y

x_pixels_savi = savi2.shape[0]  # number of pixels in x
y_pixels_savi = savi2.shape[1]  # number of pixels in y


# In[32]:


# Set up output GeoTIFF
driver = gdal.GetDriverByName('GTiff')


# In[33]:


# Create driver using output filename, x and y pixels, # of bands, and datatype
ndvi_data = driver.Create(outfile_name_ndvi,x_pixels_ndvi, y_pixels_ndvi, 1,gdal.GDT_Float32)
ndwi_data = driver.Create(outfile_name_ndwi,x_pixels_ndwi, y_pixels_ndwi, 1,gdal.GDT_Float32)
evi_data  = driver.Create(outfile_name_evi, x_pixels_evi,  y_pixels_evi,  1,gdal.GDT_Float32)
savi_data = driver.Create(outfile_name_savi,x_pixels_savi, y_pixels_savi, 1,gdal.GDT_Float32)


# In[34]:


# Set NDVI, NDWI, EVI, SAVI array as the 1 output raster band
ndvi_data.GetRasterBand(1).WriteArray(ndvi2)
ndwi_data.GetRasterBand(1).WriteArray(ndwi2)
evi_data.GetRasterBand(1).WriteArray(evi2)
savi_data.GetRasterBand(1).WriteArray(savi2)


# In[35]:


# Setting up the coordinate reference system of the output GeoTIFF
geotrans=red_link.GetGeoTransform()  # Grab input GeoTranform information
proj=red_link.GetProjection() # Grab projection information from input file


# In[36]:


# now set GeoTransform parameters and projection on the output file
ndvi_data.SetGeoTransform(geotrans) 
ndvi_data.SetProjection(proj)
ndvi_data.FlushCache()
ndvi_data=None

ndwi_data.SetGeoTransform(geotrans) 
ndwi_data.SetProjection(proj)
ndwi_data.FlushCache()
ndwi_data=None

evi_data.SetGeoTransform(geotrans) 
evi_data.SetProjection(proj)
evi_data.FlushCache()
evi_data=None

savi_data.SetGeoTransform(geotrans) 
savi_data.SetProjection(proj)
savi_data.FlushCache()
savi_data=None

