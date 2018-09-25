import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

cmap = 'Greens' #plot colour
s = 5000 #plot size

def plotScreen(shape):
    xdat, ydat, zdat, udat = np.transpose(shape)[0], np.transpose(shape)[1], np.transpose(shape)[2], np.transpose(shape)[3]
    ax = plt.subplot(221, projection='3d')
    plt.pause(0.0001)
    ax.scatter3D(xdat, ydat, zdat, c=zdat, cmap='Greens', s=5000)
    ax = plt.subplot(222, projection='3d')
    ax.scatter3D(xdat, ydat, udat, c=udat, cmap='Greens', s=5000)
    plt.pause(0.0001)
    ax = plt.subplot(223, projection='3d')
    ax.scatter3D(ydat, zdat, udat, c=udat, cmap='Greens', s=5000)
    plt.pause(0.0001)
    ax = plt.subplot(224, projection='3d')
    ax.scatter3D(xdat, zdat, udat, c=udat, cmap='Greens', s=5000)
    plt.pause(0.0001)
    plt.show()
