import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

f = 'output/ccd_{sors}.nc'
ds = nc.Dataset(f)

#Find wavelength that contains data
vals = ds.variables['data'][:,:,:]

non_zero = np.nonzero(vals)
non_zero_wavelength = non_zero[2][0]
new_vals = vals[:,:,non_zero_wavelength]
#print("checking vals: ", new_vals[:][34])
#4cmx4cm, 128x128pixels
#1cm diameter detector, in pixels
detector_rad_outer = 10.0
detector_rad_inner = detector_rad_outer - 1.0
detector_halfwidth = 40.0
detector_pixel = 128.0
pixel_rad_outer = detector_rad_outer/(detector_halfwidth/detector_pixel)
pixel_rad_inner = detector_rad_inner/(detector_halfwidth/detector_pixel)
centre = detector_pixel/2.0
total_count = 0.0
for i in range(len(new_vals)):
    for j in range(len(new_vals)):
        if ((float(i)-centre)**2 + (float(j)-centre)**2 <= (pixel_rad_outer)**2):
            if ((float(i)-centre)**2 + (float(j)-centre)**2 >= (pixel_rad_inner)**2):
                total_count += new_vals[i][j]
                #print("valid value: ", new_vals[i][j])
g = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight.txt', 'a')
g.write("{}\n".format(total_count))
print("Total count within 50mm radius of centre: ", total_count)
