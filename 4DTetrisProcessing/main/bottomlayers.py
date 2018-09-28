
shapes_list_color = [[30, 30, 30], [40, 40, 40], [50, 30, 100],
                [200, 25, 40], [10, 40, 120], [40, 40, 150], [20, 10, 40]]

def display_func2(world_coor, block_color, ax, origin, scaling):
    pushMatrix()
    translate(*origin)
    scale(1, -1, 1)
    

    for cube in world_coor:
        fill(*block_color[world_coor.index(cube)])
        stroke(255)
        pushMatrix()
        translate(*[cube[i]*scaling for i in ax])
        box(scaling)
        popMatrix()
    
    popMatrix()
    

def displayBottomLayers(bottom_layers, bottom_layers_colors, origins, scaling, current_u):
        axes = [[0,1,2],[0,3,2],[0,3,1],[1,3,2]]

        #display in xyz grid
        xyz_cubes = []
        xyz_cubes_colors = []
        for coor in bottom_layers:
            if coor[3] == current_u:
                xyz_cubes += [coor]
                xyz_cubes_colors += [bottom_layers_colors[bottom_layers.index(coor)]]
        #pos_coor_edit = []
        #pos_coor_edit += self.pos_coor
        #pos_coor_edit[1] = -pos_coor_edit[1]
        #display_func(pos_coor_edit, xyz_cubes, axes[0], origins[0], scaling)
        display_func2(xyz_cubes, xyz_cubes_colors, axes[0], origins[0], scaling)
        
        for iter in range(1, len(axes)):
            display_func2(bottom_layers, bottom_layers_colors, axes[iter], origins[iter], scaling)
