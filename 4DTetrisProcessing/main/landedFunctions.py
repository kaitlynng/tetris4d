import random
import rotate4D
import translate4D


class landed:
    def __init__(self):
        self.landed_list = []
        self.floor_list = 
    
    def rot_shape(self, plane, direction):
        self.shape_coor = rotate4D.rotate4D(self.shape_coor, plane, direction)
    
    def trans_shape(self, rotKey, direction):
        self.pos_coor = translate4D(self.shape_coor, rotKey, direction)
    
    def display(self, xyz_origin, xuz_origin, xuy_origin, yuz_origin, scaling):
        #display in xyz grid
        origins = [xyz_origin, xuz_origin, xuy_origin, yuz_origin]
        axes = [[0,1,2],[0,3,2],[0,3,1],[1,3,2]]
        fill(*self.shape_color)
        stroke(255)
        for iter in len(origins):
            pushMatrix()
            translate(*origins[iter])
            translate(*[pos_coor[i]*scaling for i in axes[iter]])
            for cube in self.shape_coor:
                pushMatrix()
                translate(*[cube[i]*scaling for i in axes[iter]])
                box(scaling)
                popMatrix()
            popMatrix()
        
    
    
