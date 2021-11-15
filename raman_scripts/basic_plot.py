import matplotlib.pyplot as plt
import numpy as np

x_pos = range(-23, 24)

weight_circ = []
weight_rect = []
f = open('/Users/lm579/Projects/Microcalcs/for_ben/Raman_weight_circle_1mm.txt','r')
for line in f:
    weight_circ.append(float(line))
f = open('/Users/lm579/Projects/Microcalcs/for_ben/Raman_weight_rectangle_1mm.txt','r')
for line in f:
    weight_rect.append(float(line))
plt.plot(x_pos, weight_circ, color='purple', label='3mm diameter circular aperture')
plt.plot(x_pos,weight_rect, color='blue', label='6mmx1mm rectangular aperture')
plt.xlabel('Position in tank (mm)')
plt.ylabel('Raman count')
plt.legend()
plt.show()
