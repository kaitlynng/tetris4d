import matmul

def transX(a):
    if a == 0:
        return [1, 0, 0, 0]
    else:
        return [0,0,0,0]

def transY(a):
    if a == 0:
        return [1, 0, 0, 0]
    else:
        return [1, 0, 0, 0]

def transY(a):
    if a == 0:
        return [1, 0, 0, 0]
    else:
        return [1, 0, 0, 0]

def transY(a):
    if a == 0:
        return [1, 0, 0, 0]
    else:
        return [1, 0, 0, 0]



def rotate4D(shape, rotKey, direction):
    # direction: +1: 0, -1: 1
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

    '''
    for i in range(0,len(shape)) :
        shape_rot[i] = matmul.matmul(switcher.get(rotKey),[shape[i][j]-mincoor_orig[j] for j in range(len(shape[i]))])
    '''

    #shift to zero
    shape_rot = [list(a-b for a,b in zip(coor, mincoor_orig)) for coor in shape]
    #matrix multiplication with transposing shape_rot
    shape_rot = matmul.matmul(switcher.get(rotKey), list(zip(*shape_rot)))
    #transpose rotated shape back
    shape_rot = list(zip(*shape_rot))

    row_sums_rot = [sum(row) for row in shape_rot]
    mincoor_rot = shape_rot[row_sums_rot.index(min(row_sums_rot))]

    '''
    for i in range(0, len(shape_rot)):
        shape_adj[i] = [shape_rot[i][j] - mincoor_rot[j] + mincoor_orig[j] for j in range(len(shape_rot[i]))]
    '''
    #shift again
    shape_adj = [list(a-b for a,b in zip(coor, mincoor_rot)) for coor in shape_rot]
    return shape_adj
