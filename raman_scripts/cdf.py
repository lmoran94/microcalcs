import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

def ncdump(nc_fid, verb=True):
    '''
    ncdump outputs dimensions, variables and their attribute information.
    The information is similar to that of NCAR's ncdump utility.
    ncdump requires a valid instance of Dataset.

    Parameters
    ----------
    nc_fid : netCDF4.Dataset
        A netCDF4 dateset object
    verb : Boolean
        whether or not nc_attrs, nc_dims, and nc_vars are printed

    Returns
    -------
    nc_attrs : list
        A Python list of the NetCDF file global attributes
    nc_dims : list
        A Python list of the NetCDF file dimensions
    nc_vars : list
        A Python list of the NetCDF file variables
    '''
    def print_ncattr(key):
        """
        Prints the NetCDF file attributes for a given key

        Parameters
        ----------
        key : unicode
            a valid netCDF4.Dataset.variables key
        """
        try:
            print("\t\ttype:", repr(nc_fid.variables[key].dtype))
            for ncattr in nc_fid.variables[key].ncattrs():
                print('\t\t%s:' % ncattr,\
                      repr(nc_fid.variables[key].getncattr(ncattr)))
        except KeyError:
            print("\t\tWARNING: %s does not contain variable attributes" % key)

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print("NetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            print('\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr)))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print("NetCDF dimension information:")
        for dim in nc_dims:
            print("\tName:", dim)
            print("\t\tsize:", len(nc_fid.dimensions[dim]))
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print("NetCDF variable information:")
        for var in nc_vars:
            if var not in nc_dims:
                print('\tName:', var)
                print("\t\tdimensions:", nc_fid.variables[var].dimensions)
                print("\t\tsize:", nc_fid.variables[var].size)
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars


f = 'output/ccd_{trs}.nc'
ds = nc.Dataset(f)

#vals = ds.variables['data']

nc_attrs, nc_dims, nc_vars = ncdump(ds)

#Find wavelength that contains data
vals = ds.variables['data'][:,:,:]

non_zero = np.nonzero(vals)
non_zero_wavelength = non_zero[2][0]
non_zero_vals = vals[vals.nonzero()]
non_zero_vals = np.array(non_zero_vals)
new_vals = vals[:,:,non_zero_wavelength]
print("shape: ", np.shape(new_vals))
print("shape0: ", np.shape(new_vals[0]))
print("shape1: ", len(new_vals[1]))
print(new_vals)

pixel_rad = 5.0/(80.0/128.0)
centre = 128.0/2.0
total_count = 0.0
number = 0
non_zeros = 0
for i in range(len(new_vals)):
    for j in range(len(new_vals)):
        if ((float(i)-centre)**2 + (float(j)-centre)**2 <= (pixel_rad)**2):
            #print("i, j: ", i, j)
            total_count += new_vals[i][j]
            if (new_vals[i][j] != 0.0):
                non_zeros +=1
            number +=1
            #print("valid value: ", new_vals[i][j])
#print("number: ", number)
#print("non_zeros: ", non_zeros)
#loc = []
#for i in range(len(non_zero)-1):
#    temp_loc = []
#    for j in range(len(non_zero[i])):
#        temp_loc.append(non_zero[i][j])
#    loc.append(temp_loc)

#loc.append(non_zero_vals)


fig, ax = plt.subplots()
im = ax.pcolormesh(new_vals, cmap=cm.Blues)
ax.set_xlabel("x location (pixels)")
ax.set_ylabel("y location (pixels)")
plt.colorbar(im, label="Raman detection, SORS")
plt.show()
