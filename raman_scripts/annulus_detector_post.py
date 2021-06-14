import netCDF4 as nc
import re
import os, os.path
import numpy as np
import numpy.ma as ma
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show


#function to read in files and then sort numerically by filename
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

directory = "/Users/lm579/Projects/Microcalcs/output/ccd_sors_map/"
filenames = []
count=0

for file in sorted(os.listdir(directory), key=numericalSort):
    if file.endswith(".nc"):
        count+=1
        f = open(directory+file,'r')
        filenames.append(os.path.basename(f.name))
        #print("file: ", os.path.basename(f.name))
        ds = nc.Dataset(directory+file)
        vals = ds.variables['data'][:,:,:]
        #vals_trs = dds.variables['data'][:,:,:]

        non_zero = np.nonzero(vals)
        #non_zero_trs = np.nonzero(vals_trs)
        non_zero_wavelength = non_zero[2][0]
        #non_zero_wavelength_trs = non_zero_trs[2][0]
        new_vals = vals[:,:,non_zero_wavelength]
        #new_vals_trs = vals_trs[:,:,non_zero_wavelength_trs]

        #8cmx8cm, 128x128pixels
        #1mm thick annulus detector, in pixels
        detector_rad_outer = 10.0
        detector_rad_inner = detector_rad_outer - 1.0
        ccd_width = 80.0
        ccd_pixel = 128.0
        pixel_rad_outer = detector_rad_outer/(ccd_width/ccd_pixel)
        pixel_rad_inner = detector_rad_inner/(ccd_width/ccd_pixel)
        centre = ccd_pixel/2.0
        total_count = 0.0
        for i in range(len(new_vals)):
            for j in range(len(new_vals)):
                if ((float(i)-centre)**2 + (float(j)-centre)**2 <= (pixel_rad_outer)**2):
                    if ((float(i)-centre)**2 + (float(j)-centre)**2 >= (pixel_rad_inner)**2):
                        total_count += new_vals[i][j]
                        #print("valid value: ", new_vals[i][j])
        g = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight_annulus_10mm.txt', 'a')
        g.write("{}\n".format(total_count))
        print("Total count within 50mm radius of centre: ", total_count)
