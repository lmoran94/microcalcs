import matplotlib.pyplot as plt
import numpy as np
import sys
from itertools import repeat
import matplotlib.colors as colors
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

fig, ax = plt.subplots()

#positions for 1mm sphere
#x_pos = list(range(-23, 24, 1))
#og_lenx = len(x_pos)
#y_pos = list(range(-38, 39, 2))
#og_leny = len(y_pos)
#x_pos=x_pos*og_leny
#y_pos = y_pos*og_lenx
#x,y = np.mgrid[-23.5:24.5:1, -39:40:2]
#print(len(range(-23, 25, 1)))
#print(len(range(-39,40,2)))

#positions for 1cm sphere
x_pos = list(range(-19, 20, 1))
og_lenx = len(x_pos)
y_pos = list(range(-32, 33, 2))
og_leny = len(y_pos)
x_pos=x_pos*og_leny
y_pos = y_pos*og_lenx
x,y= np.mgrid[-19.5:20.5:1, -33:35:2]
print(len(range(-19,21,1)))
print(len(range(-33,35,2)))

#positions for 4cm linear
#x_pos = list(range(-23, 24, 1))
#og_lenx = len(x_pos)
#y_pos = list(range(-19, 21, 2))
#og_leny = len(y_pos)
#x_pos=x_pos*og_leny
#y_pos = y_pos*og_lenx



weight = []
number = int(sys.argv[1])
filename = '/Users/lm579/Projects/Microcalcs/output/1mm_beam/1cm_dia_10calc/Raman_weight_annulus_%s.txt' %number
#f = open('/Users/lm579/Projects/Microcalcs/output/1cm_sphere_1mm_spot_redo/Raman_weight_circle_5.txt','r')
f = open(filename,'r')
for line in f:
    weight.append(float(line))


shaped_weights = np.reshape(weight, (og_lenx, og_leny))
print(np.shape(shaped_weights))

#print("shaped weights: ", np.shape(shaped_weights))
#shaped_weights = np.transpose(shaped_weights)
#shaped_weights = np.flip(shaped_weights)


#im = ax.pcolormesh(shaped_weights,  norm=colors.LogNorm(vmin=shaped_weights.min(), vmax=shaped_weights.max()))

im = ax.pcolormesh(x,y,shaped_weights, shading='auto', cmap=plt.cm.get_cmap('gnuplot'), norm=colors.LogNorm(vmin=shaped_weights.min(), vmax=shaped_weights.max()))
#im = ax.imshow(np.transpose(shaped_weights),  cmap=plt.cm.get_cmap('gnuplot'), norm=colors.LogNorm(vmin=shaped_weights.min(), vmax=shaped_weights.max()))
ax.set_xlabel("x location (mm)", fontsize=14)
ax.set_ylabel("y location (mm)", fontsize=14)

#labels in centre of pixel instead of edge

#lines to indicate laser and detector locations
#due to above movement: add 1.5 to expected y values
#TRS
#ax.hlines(y=5, xmin=-23.5, xmax=-23, linewidth=2, color='r')
#ax.hlines(y=-5, xmin=-23.5, xmax=-23, linewidth=2, color='r')
#ax.hlines(y=number, xmin=23.5, xmax=23, linewidth=2, color='k')
#ax.hlines(y=-number, xmin=23.5, xmax=23, linewidth=2, color='k')


#SORS
ax.hlines(y=0.5, xmin=-19.5, xmax=-19, linewidth=2, color='r')
ax.hlines(y=-0.5, xmin=-19.5, xmax=-19, linewidth=2, color='r')
ax.hlines(y=number, xmin=-19, xmax=-19.5, linewidth=2, color='k')
ax.hlines(y=number-1, xmin=-19, xmax=-19.5, linewidth=2, color='k')
ax.hlines(y=-number, xmin=-19, xmax=-19.5, linewidth=2, color='k')
ax.hlines(y=-number+1, xmin=-19, xmax=-19.5, linewidth=2, color='k')



plt.colorbar(im, label="Raman detection")
plt.savefig('/Users/lm579/Projects/Calcs_results/1mm_beam/1cm_dia_10calc/annulus_%s.png' %number, bbox_inches='tight')
plt.show()
