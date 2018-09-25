# rotating the planes
import numpy as np

'''
def rotXY(a):
    return np.array([
        [np.cos(a),np.sin(a),0,0],
        [-np.sin(a), np.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

def rotYZ(a):
    return np.array([
        [1,0,0,0],
        [0, np.cos(a),np.sin(a), 0],
        [0, -np.sin(a), np.cos(a), 0],
        [0, 0, 0, 1]])

def rotXZ(a):
    return np.array([
        [np.cos(a),0,-np.sin(a),0],
        [0, 1,0, 0],
        [np.sin(a), 0, np.cos(a), 0],
        [0, 0, 0, 1]])

def rotXU(a):
    return np.array([
        [np.cos(a),0,0,np.sin(a)],
        [0,1,0,0],
        [0, 0, 1, 0],
        [-np.sin(a), 0, 0, np.cos(a)]])

def rotYU(a):
    return np.array([
        [1,0,0,0],
        [0,np.cos(a),0,-np.sin(a)],
        [0, 0, 1, 0],
        [0,np.sin(a), 0, np.cos(a)]])

def rotZU(a):
    return np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0, 0, np.cos(a), -np.sin(a)],
    [0,np.sin(a), 0, np.cos(a)]])
'''

def rotXY(a):
    if a == 0:
        return np.array([
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
    else:
        return np.array([
            [0,-1,0,0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])

def rotYZ(a):
    if a == 0:
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, -1, 0, 0],
            [0, 0, 0, 1]])
    else:
        return np.array([
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])

def rotXZ(a):
    if a == 0:
        return np.array([
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1]])
    else:
        return np.array([
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 0, 1]])

def rotXU(a):
    if a == 0:
        return np.array([
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-1, 0, 0, 0]])
    else:
        return np.array([
            [0, 0, 0, -1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]])

def rotYU(a):
    if a == 0:
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 0, -1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]])
    else:
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, -1, 0, 0]])

def rotZU(a):
    if a == 0:
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, -1],
            [0, 1, 0, 0]])
    else:
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, -1, 0, 1]])

def rotate4D(shape, rotKey, direction):
    # direction: +90deg: 0, -90deg: 1
    switcher = {
        0: rotXY(direction),
        1: rotYZ(direction),
        2: rotXZ(direction),
        3: rotXU(direction),
        4: rotYU(direction),
        5: rotZU(direction),
    }

#    mean = np.sum(shape, axis=0)/np.shape(shape)[0]
#    return np.dot((shape-mean), switcher.get(rotKey))+mean

    # move to center
    shape_centred = np.zeros(np.shape(shape))
    print("hi")
    print(shape)
    for i in range(0, np.shape(shape)[0]):
        shape_centred[i] = shape[i]-shape[0]
        shape_centred[i] = np.matmul([shape[i]-shape[0]], switcher.get(rotKey))
        shape_centred[i] += shape[0]
    print(shape_centred)
    return shape_centred

'''
    shape_rotated = np.dot(switcher.get(rotKey), shape_centred)
    print(shape_rotated)
    for i in range(0, np.shape(shape_rotated)[0]):
        shape_rotated[i] += shape[0]
    return shape_rotated
'''
