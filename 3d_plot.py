from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

points = pandas.read_csv('og_calc.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = points['x'].values
y = points['y'].values
z = points['z'].values

#  x   y   z
# 1.1,1.2,1.3
# 2.1,2.2,2.3
# 3.1,3.2,3.3
# 4.1,4.2,4.3

ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlim(-0.005, 0.005)
ax.set_ylim(-0.005, 0.005)
ax.set_zlim(-0.005, 0.005)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
