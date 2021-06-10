import matplotlib.pyplot as plt
import numpy as np
from itertools import repeat
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar, axis, title, show

x_pos = list(range(-23, 14, 1))
print("len1: ", len(x_pos))
x_pos = x_pos*38
y_pos = list(range(-38, 38, 2))
print("len2: ", len(y_pos))
y_pos = y_pos*37

print("len x_pos: ", len(x_pos))

print("len y_pos: ", len(y_pos))

weight = []
f = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight_post_trs.txt','r')
for line in f:
    weight.append(float(line))

#print("type: ", np.type(x_pos))
list = []

list.append(x_pos)
list.append(y_pos)
list.append(weight)

#print("type: ", np.shape(list))
array = np.array(list)
#print("array: ", np.shape(array))
print("len: ", len(array[0]))
print("len: ", len(array[1]))
print("len: ", len(array[2]))
#print("list: ", list)

plt.tricontourf(array[0], array[1], array[2])
#fig, ax = plt.subplots()
#im = ax.pcolormesh(array[0])
ax.set_xlabel("x location (pixels)")
ax.set_ylabel("y location (pixels)")
plt.colorbar(im, label="Raman detection, SORS")
plt.show()
