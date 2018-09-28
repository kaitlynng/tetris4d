import numpy as np
world_blocks_coor = []
#list of numpy arrays

world_blocks_colour = []
#list of python arrays

def initWorld(size):
    #size is a list for [x, y, z, u]
    fig, axes = plt.subplots(2, 2, subplot_kw=dict(projection='3d'))
    fig2, ax = plt.subplots(1, 1, subplot_kw=dict(projection='3d'))

def blockSet(block_coor, block_colour):
    world_blocks_coor += [block_coor]
    world_blocks_colour += [block_colour]
