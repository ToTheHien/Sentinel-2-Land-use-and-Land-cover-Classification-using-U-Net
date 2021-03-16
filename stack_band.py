#!/usr/bin/env python
# coding: utf-8

# In[32]:


import glob
import numpy as np
from osgeo import gdal
from PIL import Image


# In[33]:


in_dir = '/home/thehien/Landsat-8/LC08_L2SP_124052_20200115_20200824_02_T1/'


# In[34]:


b1_file = glob.glob(in_dir + '**B1.TIF')
b2_file = glob.glob(in_dir + '**B2.TIF') 
b3_file = glob.glob(in_dir + '**B3.TIF')
b4_file = glob.glob(in_dir + '**B4.TIF') 
b5_file = glob.glob(in_dir + '**B5.TIF') 
b6_file = glob.glob(in_dir + '**B6.TIF') 
b7_file = glob.glob(in_dir + '**B7.TIF') 


# In[35]:


def norm(band):
    band_min, band_max = band.min(), band.max()
    return ((band - band_min)/(band_max - band_min))


# In[36]:


for i in range(len(b1_file)):   
    # Open each band using gdal
    b1_link = gdal.Open(b1_file[i])
    b2_link = gdal.Open(b2_file[i])
    b3_link = gdal.Open(b3_file[i])
    b4_link = gdal.Open(b4_file[i])
    b5_link = gdal.Open(b5_file[i])
    b6_link = gdal.Open(b6_file[i])
    b7_link = gdal.Open(b7_file[i])
    
    # call the norm function on each band as array converted to float
    b1 = norm(b1_link.ReadAsArray().astype(np.float))
    b2 = norm(b2_link.ReadAsArray().astype(np.float))
    b3 = norm(b3_link.ReadAsArray().astype(np.float))
    b4 = norm(b4_link.ReadAsArray().astype(np.float))
    b5 = norm(b5_link.ReadAsArray().astype(np.float))
    b6 = norm(b6_link.ReadAsArray().astype(np.float))
    b7 = norm(b7_link.ReadAsArray().astype(np.float))
    
    # Stack
    stack = np.dstack((b1,b2,b3,b4,b5,b6,b7))
    del b1, b2, b3, b4, b5, b6, b7
    
    # Export Stack as TIFF file
    Image.fromarray(stack).save(b1_file[i].split('_01_')[0]+'_stack.tif')


# In[ ]:




