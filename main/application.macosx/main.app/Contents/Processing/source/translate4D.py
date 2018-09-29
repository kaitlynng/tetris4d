def translate4D(coor, transKey, direction):
    trans_vec = [0,0,0,0]
    trans_vec[transKey] = direction
    shape_adj = list(a+b for a,b in zip(coor, trans_vec))
    return shape_adj
