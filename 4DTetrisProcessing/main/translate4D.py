def transX(a):
    if a == 0:
        return [1, 0, 0, 0]
    else:
        return [-1, 0, 0, 0]

def transY(a):
    if a == 0:
        return [0, 1, 0, 0]
    else:
        return [0, -1, 0, 0]

def transZ(a):
    if a == 0:
        return [0, 0, 1, 0]
    else:
        return [0, 0, -1, 0]

def transU(a):
    if a == 0:
        return [0, 0, 0, 1]
    else:
        return [0, 0, 0, -1]

def translate4D(shape, transKey, direction):
    # direction: +1unit: 0, -1unit: 1
    switcher = {
        0: transX(direction),
        1: transY(direction),
        2: transZ(direction),
        3: transU(direction),
    }
    trans_vec = switcher.get(transKey)
    shape_adj = [list(a+b for a,b in zip(coor, trans_vec)) for coor in shape] 
    return shape_adj
