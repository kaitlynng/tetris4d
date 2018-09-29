import matmul
"""
Handles rotations

"""


def rotXY(a):
    if a == 0:
        return [
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
    else:
        return [
            [0,-1,0,0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

def rotYZ(a):
    if a == 0:
        return [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, -1, 0, 0],
            [0, 0, 0, 1]]
    else:
        return [
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]]

def rotXZ(a):
    if a == 0:
        return [
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1]]
    else:
        return [
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 0, 1]]

def rotXU(a):
    if a == 0:
        return [
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-1, 0, 0, 0]]
    else:
        return [
            [0, 0, 0, -1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]]

def rotYU(a):
    if a == 0:
        return [
            [1, 0, 0, 0],
            [0, 0, 0, -1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]]
    else:
        return [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, -1, 0, 0]]

def rotZU(a):
    if a == 0:
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, -1],
            [0, 0, 1, 0]]
    else:
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, -1, 0]]

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


# move to center
    row_sums = [sum(row) for row in shape]
    mincoor_orig = shape[row_sums.index(min(row_sums))]

    #shift to zero
    shape_rot = [list(a-b for a,b in zip(coor, mincoor_orig)) for coor in shape]
    #matrix multiplication with transposing shape_rot
    shape_rot = matmul.matmul(switcher.get(rotKey), list(zip(*shape_rot)))
    #transpose rotated shape back
    shape_rot = list(zip(*shape_rot))

    row_sums_rot = [sum(row) for row in shape_rot]
    mincoor_rot = shape_rot[row_sums_rot.index(min(row_sums_rot))]

    #shift again
    shape_adj = [list(a-b for a,b in zip(coor, mincoor_rot)) for coor in shape_rot]
    return shape_adj
