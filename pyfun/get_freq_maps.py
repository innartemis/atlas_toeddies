################################################################################
# ----------------------------------------------------------------------------#
# LMD (2022) - Artemis Ioannou
# ----------------------------------------------------------------------------#
################################################################################
import math as math
import numpy as np
from scipy.stats import binned_statistic_2d


def get_freqMAP(xpoints,ypoints):
    #compute frequency map of xypoints in lon/lat grid
    grid_x, grid_y= np.mgrid[-180:180, -90:90]
    xlim, ylim =[-180,180], [-90,90]
    vector_x,vector_y = np.arange(min(xlim),max(xlim)+1,1),np.arange(min(ylim),max(ylim)+1,1)
    grid_z,_,_ = np.histogram2d(xpoints,ypoints,bins=[vector_x,vector_y])
    return (grid_x, grid_y,grid_z)


def get_freqMAP_var(xpoints,ypoints,zpoints):
    #compute mean frequency map of variable zpoints in lon/lat grid
    grid_x, grid_y= np.mgrid[-180:180, -90:90]
    xlim, ylim =[-180,180], [-90,90]
    vector_x,vector_y = np.arange(min(xlim),max(xlim)+1,1),np.arange(min(ylim),max(ylim)+1,1)
    ret = binned_statistic_2d(xpoints,ypoints,zpoints,statistic=np.nanmean, bins=[vector_x,vector_y])
    grid_z=ret.statistic
    return (grid_x, grid_y,grid_z)




