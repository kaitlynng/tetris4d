import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from rotate4D import *
from plotCube import *

a = 0

# plt.ion()

#3d shapes
shape1 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]])
shape2 = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

#4d shapes
shape3 = np.array([[0,0,0,1], [0,1,0,0],[1,0,0,0],[0,0,1,0]])
# testshape = np.array([[0,0,0,0]])

print(shape3)
print(rotate4D(shape3, 3, 90))
print(rotate4D(shape3, 5, -90))
print(rotate4D(shape3, 1, 90))

#rotating plot NOT WORKING
#while True:
#    plotShape(shape3)
#    print('hi')
#    shape3 = rotate4D(shape3, 0, 90)
#    time.sleep(1)
#    plt.clf()

plotShape(shape3)
