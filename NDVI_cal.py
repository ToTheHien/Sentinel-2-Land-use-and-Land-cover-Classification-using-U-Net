#!/usr/bin/env python
# coding: utf-8

# In[2]:


import rasterio 
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


import os
filedir = '/home/thehien/Downloads/Landsat-8/LC08_L2SP_124052_20200115_20200824_02_T1/'
os.listdir(filedir)


# In[32]:


band4 = rasterio.open(filedir + 'LC08_L2SP_124052_20200115_20200824_02_T1_SR_B4.TIF') #red
band5 = rasterio.open(filedir + 'LC08_L2SP_124052_20200115_20200824_02_T1_SR_B5.TIF') #nir


# In[33]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
plot.show(band4, ax=ax1, cmap='Blues') #red
plot.show(band5, ax=ax2, cmap='Blues') #nir
fig.tight_layout()


# In[34]:


red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

nir


# In[35]:


ndvi=np.where(
    (nir+red)==0.,
    0,
    (nir-red)/(nir+red)
)

ndvi


# In[37]:


ndviImage = rasterio.open(filedir + 'Output/ndviImage.tiff','w',driver='Gtiff',
                         width = band4.width, height = band4.height,
                         count = 1,
                         crs = band4.crs,
                         dtype = 'float64' 
                         )
ndviImage.write(ndvi,1)
ndviImage.close()


# In[38]:


ndvi = rasterio.open(filedir + 'Output/ndviImage.tiff')
plot.show(ndvi)

