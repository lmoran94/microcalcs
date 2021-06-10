import matplotlib.pyplot as plt
import numpy as np

x_pos = range(-23, 23)

weight = []
f = open('/Users/lm579/Projects/Microcalcs/output/Raman_weight_post.txt','r')
for line in f:
    weight.append(float(line))

plt.plot(x_pos, weight)
plt.show()
