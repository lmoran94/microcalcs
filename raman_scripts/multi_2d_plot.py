import matplotlib.pyplot as plt
import numpy as np
import re
from itertools import repeat
import matplotlib.colors as colors
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

#positions for 1mm sphere
#x_pos = list(range(-23, 24, 1))
#og_lenx = len(x_pos)
#y_pos = list(range(-38, 40, 2))
#og_leny = len(y_pos)
#x_pos=x_pos*og_leny
#y_pos = y_pos*og_lenx

#positions for 1cm sphere
#x_pos = list(range(-14, 15, 1))
#og_lenx = len(x_pos)
#y_pos = list(range(-28, 32, 2))
#og_leny = len(y_pos)
#x_pos=x_pos*og_leny
#y_pos = y_pos*og_lenx

#positions for 4cm linear
x_pos = list(range(-23, 24, 1))
og_lenx = len(x_pos)
y_pos = list(range(-19, 21, 2))
og_leny = len(y_pos)
x_pos=x_pos*og_leny
y_pos = y_pos*og_lenx

#function to read in files and then sort numerically by filename
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#directory = "/home/laura/Projects/microcalcs/output/1cm_sphere_1mmspot/"
#filenames = []
#count=0
weight = []

#for file in sorted(os.listdir(directory), key=numericalSort):
#    if file.endswith(".txt"):
#        count+=1
#        f = open(directory+file,'r')
#        filenames.append(os.path.basename(f.name))
#        #print("file: ", os.path.basename(f.name))
#        ds = nc.Dataset(directory+file)
#        vals = ds.variables['data'][:,:,:]
        #vals_trs = dds.variables['data'][:,:,:]


weight_1 = []
f = open('/Users/lm579/Projects/Microcalcs/output/4cm_linear_1mmspot/Raman_weight_circle_5.txt','r')
for line in f:
    weight_1.append(float(line))
weight_2 = []
g = open('/Users/lm579/Projects/Microcalcs/output/4cm_linear_1mmspot/Raman_weight_circle_20.txt', 'r')
for line in g:
    weight_2.append(float(line))
#print("type: ", np.type(x_pos))
list = []

list.append(x_pos)
list.append(y_pos)
list.append(weight)
#shaped_weights = np.reshape(weight, (og_lenx, og_leny))
shaped_weights_1 = np.reshape(weight_1, (og_lenx, og_leny))
shaped_weights_2 = np.reshape(weight_2, (og_lenx, og_leny))
#print("type: ", np.shape(list))
array = np.array(list)
#print("array: ", np.shape(array))
#print("len: ", len(array[0]))
#print("len: ", len(array[1]))
#print("len: ", len(array[2]))
#print("list: ", list)

minmin = np.min([shaped_weights_1, shaped_weights_2])
maxmax = np.max([shaped_weights_1, shaped_weights_2])

fig, axes = plt.subplots(nrows=1, ncols=2)
#im = ax.pcolormesh(shaped_weights)
im1 = axes[0].pcolormesh(shaped_weights_1, vmin=minmin, vmax=maxmax)
im2 = axes[1].pcolormesh(shaped_weights_2, vmin=minmin, vmax=maxmax)
#im1 = axes[0].imshow(shaped_weights_1, norm=colors.LogNorm(vmin=minmin, vmax=maxmax))
#im2 = axes[1].imshow(shaped_weights_2, norm=colors.LogNorm(vmin=minmin, vmax=maxmax))

#ax.set_xlabel("x location (mm)")
#ax.set_ylabel("y location (mm)")
fig.colorbar(im2, label="Raman detection, TRS")
plt.show()

#fig, ax = plt.subplots()
#im = ax.pcolormesh(shaped_weights)
#im = ax.pcolormesh(shaped_weights, norm=colors.LogNorm(vmin=shaped_weights.min(), vmax=shaped_weights.max()))
#ax.set_xlabel("x location (mm)")
#ax.set_ylabel("y location (mm)")
#plt.colorbar(im, label="Raman detection, SORS")
#plt.show()
