def translate4D(pos_coor, transKey, direction):
    trans_vec = [0,0,0,0]
    trans_vec[transKey] = direction
    shape_adj = [list(a+b for a,b in zip(coor, trans_vec)) for coor in pos_coor] 
    return shape_adj
