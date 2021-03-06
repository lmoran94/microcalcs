import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

f = 'output/ccd_{sors}.nc'
g = 'output/ccd_{trs}.nc'
ds = nc.Dataset(f)
dds = nc.Dataset(g)

#Find wavelength that contains data
vals = ds.variables['data'][:,:,:]
vals_trs = dds.variables['data'][:,:,:]

non_zero = np.nonzero(vals)
non_zero_trs = np.nonzero(vals_trs)
non_zero_wavelength = non_zero[2][0]
non_zero_wavelength_trs = non_zero_trs[2][0]
new_vals = vals[:,:,non_zero_wavelength]
new_vals_trs = vals_trs[:,:,non_zero_wavelength_trs]
#print("checking vals: ", new_vals[:][34])
#8cmx8cm, 128x128pixels
#1cm diameter detector, in pixels
detector_rad = 5.0
ccd_width = 80.0
ccd_pixel = 128.0
pixel_rad = detector_rad/(ccd_width/ccd_pixel)
centre = ccd_pixel/2.0
total_count = 0.0
total_count_trs = 0.0
for i in range(len(new_vals)):
    for j in range(len(new_vals)):
        if ((float(i)-centre)**2 + (float(j)-centre)**2 <= (pixel_rad)**2):
            total_count += new_vals[i][j]
            total_count_trs += new_vals_trs[i][j]
            #print("valid value: ", new_vals[i][j])
new_f = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight_sors.txt', 'a')
new_f.write("{}\n".format(total_count))
print("Total count within 50mm radius of centre (SORS): ", total_count)

new_g = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight_trs.txt', 'a')
new_g.write("{}\n".format(total_count_trs))
print("Total count within 50mm radius of centre (SORS): ", total_count_trs)
