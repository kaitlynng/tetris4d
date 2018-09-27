import matmul

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
            [0, 1, 0, 0]]
    else:
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, -1, 0, 1]]

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
    shape_rot = [[0 for col in range(len(shape[0]))] for row in range(len(shape))]
    shape_adj = [[0 for col in range(len(shape[0]))] for row in range(len(shape))]
    row_sums = [sum(row) for row in shape]
    mincoor_orig = shape[row_sums.index(min(row_sums))]

    for i in range(0,len(shape)) :
        shape_rot[i] = matmul.matmul(switcher.get(rotKey),[shape[i][j]-mincoor_orig[j] for j in range(len(shape[i]))])

    row_sums_rot = [sum(row) for row in shape_rot]
    mincoor_rot = shape_rot[row_sums_rot.index(min(row_sums_rot))]

    for i in range(0, len(shape_rot)):
        shape_adj[i] = [shape_rot[i][j] - mincoor_rot[j] + mincoor_orig[j] for j in range(len(shape_rot[i]))]

    return shape_adj

rotate4D([[0,0,0,0],[1,0,0,0]], 0, 1)













