import random
import rotate4D
import translate4D

shapes_list_coor = [[[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]],
                    [[0,0,0,0],[1,0,0,0],[2,0,0,0],[2,0,1,0]],
                    [[0,0,0,0],[1,0,0,0],[1,0,1,0],[2,0,1,0]],
                    [[0,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,0,0]],
                    [[0,0,0,0],[1,0,0,0],[2,0,0,0],[1,1,0,0]],
                    [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]],
                    [[0,0,0,0],[0,1,0,0],[0,1,1,0],[1,1,1,0]]]
shapes_list_color = [[30, 30, 30], [40, 40, 40], [50, 30, 100],
                      [200, 25, 40], [10, 40, 120], [40, 40, 150], [20, 10, 40]]

def display_func(pos_coor, shape_coor, ax, origin, scaling):
    pushMatrix()
    translate(*origin)
    translate(*[pos_coor[i]*scaling for i in ax])
    for cube in shape_coor:
        pushMatrix()
        translate(*[cube[i]*scaling for i in ax])
        box(scaling)
        popMatrix()
    popMatrix()

class Shape:
    def __init__(self, pos_coor):
        self.shape_coor = random.choice(shapes_list_coor)
        self.shape_color = shapes_list_color[shapes_list_coor.index(self.shape_coor)]
        self.pos_coor = pos_coor #in world coordinates
    
    def rotShape(self, plane, direction):
        self.shape_coor = rotate4D.rotate4D(self.shape_coor, plane, direction)
    
    def transShape(self, rotKey, direction):
        self.pos_coor = translate4D.translate4D(self.pos_coor, rotKey, direction)
    
    def displayShape(self, origins, scaling, current_u):
        axes = [[0,1,2],[0,3,2],[0,3,1],[1,3,2]]
        fill(*self.shape_color)
        stroke(255)

        for iter in range(len(origins)):
            pushMatrix()
            translate(*origins[iter])
            translate(*[self.pos_coor[i]*scaling for i in axes[iter]])
            for cube in self.shape_coor:
                pushMatrix()
                translate(*[cube[i]*scaling for i in axes[iter]])
                box(scaling)
                popMatrix()
            popMatrix()

        #display in xyz grid
        xyz_cubes = []
        for coor in self.shape_coor:
            if coor[3]-self.shape_coor[0][3]+self.pos_coor[3] == current_u:
                xyz_cubes += [coor]
        pos_coor_edit = []
        pos_coor_edit += self.pos_coor
        pos_coor_edit[1] = -pos_coor_edit[1]
        display_func(pos_coor_edit, xyz_cubes, axes[0], origins[0], scaling)
        
        for iter in range(1, len(axes)):
            display_func(self.pos_coor, self.shape_coor, axes[iter], origins[iter], scaling)

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


