import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from rotate4D import *
from plotCube import *

a = 0

# plt.ion()

#4d shapes
shape3 = np.array([[0,0,0,1], [0,1,0,0],[1,0,0,0],[0,0,1,0]])
shape4 = np.array([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,1,1,0]])
shape5 = np.array([[0,0,0,0],[0,1,0,0]])
# testshape = np.array([[0,0,0,0]])

#rotating plot NOT WORKING
#while True:
#    plotShape(shape3)
#    print('hi')
#    shape3 = rotate4D(shape3, 0, 90)
#    time.sleep(1)
#    plt.clf()

# plotShape(shape5)

plotShape(rotate4D(shape3, 3, 90))
