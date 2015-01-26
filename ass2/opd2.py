import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # noqa
from matplotlib import cm


def f(x, y):
    x1 = x - 1
    x2 = x + 1
    return (np.log(np.sqrt((x2*x2) + (y*y))) -
            np.log(np.sqrt((x1*x1) + (y*y))))
x = np.linspace(-8.0, 8.0, 100)
y = np.linspace(-4.0, 4.0, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)
print(z)

fig = plt.figure(figsize=(24, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax1.contour(x, y, z, cmap=cm.coolwarm)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')

ax2 = fig.add_subplot(1, 2, 2)
p2 = ax2.contourf(x, y, z, levels=4, cmap=cm.coolwarm)
ax2.locator_params(nbins=5)
fig.colorbar(p2)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')

plt.show()
