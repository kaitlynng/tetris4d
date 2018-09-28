import random
import rotate4D
import translate4D
import time

shapes_list_coor = [[[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]],
                    [[0,0,0,0],[1,0,0,0],[2,0,0,0],[2,0,1,0]],
                    [[0,0,0,0],[1,0,0,0],[1,0,1,0],[2,0,1,0]],
                    [[0,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,0,0]],
                    [[0,0,0,0],[1,0,0,0],[2,0,0,0],[1,1,0,0]],
                    [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]],
                    [[0,0,0,0],[0,1,0,0],[0,1,1,0],[1,1,1,0]]]
shapes_list_color = [[255, 157, 242], [175, 255, 234], [245, 255, 175],
                      [255, 175, 175], [200, 177, 255], [135, 255, 151], [165, 192, 255]]

block_stroke = 0
transparency = 60

def display_func(pos_coor, shape_coor, ax, origin, scaling):
    pushMatrix()
    translate(scaling/2, -scaling/2, scaling/2)
    
    pushMatrix()
    translate(*origin)
    scale(1, -1, 1)
    
    translate(*[pos_coor[i]*scaling for i in ax])
    for cube in shape_coor:
        pushMatrix()
        translate(*[cube[i]*scaling for i in ax])
        box(scaling)
        popMatrix()
    popMatrix()
    
    popMatrix()

class Shape:
    def __init__(self, pos_coor, time_delta):
        self.shape_coor = random.choice(shapes_list_coor)
        self.shape_color = shapes_list_color[shapes_list_coor.index(self.shape_coor)]
        self.pos_coor = pos_coor #in world coordinates
        self.prev_time = 0
        self.time_delta = time_delta
        self.check_iter = 0 #for debugging
        
    def rotShape(self, plane, direction):
        self.shape_coor = rotate4D.rotate4D(self.shape_coor, plane, direction)
    
    def transShape(self, rotKey, direction):
        self.pos_coor = translate4D.translate4D(self.pos_coor, rotKey, direction)
    
    
    def displayShape(self, origins, scaling, current_u):
        global block_stroke
        axes = [[0,1,2],[0,3,2],[0,3,1],[1,3,2]]
        fill(*self.shape_color)
        stroke(block_stroke)

        #display in xyz grid
        for i in range(3):
            xyz_cubes = []
            for coor in self.shape_coor:
                if coor[3]-self.shape_coor[0][3]+self.pos_coor[3] == current_u[i]:
                    xyz_cubes += [coor]
        
            display_func(self.pos_coor, xyz_cubes, axes[0], origins[i], scaling)

        for iter in range(1, len(axes)):
            display_func(self.pos_coor, self.shape_coor, axes[iter], origins[iter+2], scaling)

    def checkBounds(self, worldSize):
        #list of points in world coords
        worldcoords = [list(a+b for a,b in zip(j, self.pos_coor)) for j in self.shape_coor]
        for i in range(4):
            min_coord = min([j[i] for j in worldcoords])
            max_coord = max([j[i] for j in worldcoords])
            while max_coord >= worldSize[i]:
                self.pos_coor = translate4D.translate4D(self.pos_coor, i, -1)
                max_coord -=1
            while min_coord < 0:
                self.pos_coor = translate4D.translate4D(self.pos_coor, i, 1)
                min_coord +=1
                
    def checkStop(self, bottom_layers, bottom_layers_colors):
        global transparency
        stop_shape = False
        if time.time()-self.prev_time > self.time_delta:
            worldcoords = tuple((tuple(a+b for a,b in zip(j, self.pos_coor)) for j in self.shape_coor))
            worldcoords_next = [list(coor) for coor in worldcoords]
            for coor in worldcoords_next:
                coor[3] -= 1
                if coor in bottom_layers:
                    stop_shape = True
                    break
                if coor[3] < 0:
                    stop_shape = True
                    break
            if stop_shape:
                worldcoords = [list(coor) for coor in worldcoords]
                bottom_layers += worldcoords
                bottom_layers_colors += [self.shape_color+[transparency] for i in range(len(self.shape_coor))]
            else:
                self.transShape(3,-1)
                self.prev_time = time.time()
        return stop_shape, bottom_layers, bottom_layers_colors
            
        
            
        
        
