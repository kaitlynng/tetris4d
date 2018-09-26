import time
import numpy as np
import random as rand
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from rotate4D import *
from plotCube import *

# plt.ion()

#4d shapes
shape3 = np.array([[0,0,0,0],[0,0,0,1], [0,1,0,0],[1,0,0,0],[0,0,1,0]])
shape4 = np.array([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,1,1,0]])
shape5 = np.array([[0,0,0,0],[0,1,0,0]])
# testshape = np.array([[0,0,0,0]])

shapes = np.array([[[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]],
                   [[0,0,0,0],[1,0,0,0],[2,0,0,0],[2,0,1,0]],
                   [[0,0,0,0],[1,0,0,0],[1,0,1,0],[2,0,1,0]],
                   [[0,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,0,0]],
                   [[0,0,0,0],[1,0,0,0],[2,0,0,0],[1,1,0,0]],
                   [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]],
                   [[0,0,0,0],[0,1,0,0],[0,1,1,0],[1,1,1,0]],
                   [[0,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,1,0]]])

#rotating plot NOT WORKING
#while True:
#    plotShape(shape3)
#    print('hi')
#    shape3 = rotate4D(shape3, 0, 90)
#    time.sleep(1)
#    plt.clf()

colour = [rand.random(), rand.random(), rand.random(), 0.1]

for x in range(0,8):
    plotShape(shapes[x,:,:], colour)

#plotShape_slice(shape3, 0, colour)

#plotShape(rotate4D(shape3, 1, 0), colour)
#plotShape_slice(rotate4D(shape3, 1, 0), 0, colour)

plt.show()
