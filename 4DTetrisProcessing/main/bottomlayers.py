bottom_layers_stroke = 255

def display_func2(world_coor, block_color, ax, origin, scaling):
    pushMatrix()
    translate(scaling/2, -scaling/2, scaling/2)
    
    pushMatrix()
    translate(*origin)
    scale(1, -1, 1)
    
    for cube in world_coor:
        fill(*block_color[world_coor.index(cube)])
        stroke(bottom_layers_stroke)
        pushMatrix()
        translate(*[cube[i]*scaling for i in ax])
        box(scaling)
        popMatrix()
    
    popMatrix()
    popMatrix()

def displayBottomLayers(bottom_layers, bottom_layers_colors, origins, scaling, current_u):
        axes = [[0,1,2],[0,3,2],[0,3,1],[1,3,2]]

        #display in xyz grid
        for i in range(3):
            xyz_cubes = []
            xyz_cubes_colors = []
            for coor in bottom_layers:
                if coor[3] == current_u[i]:
                    xyz_cubes += [coor]
                    xyz_cubes_colors += [bottom_layers_colors[bottom_layers.index(coor)]]
        
            display_func2(xyz_cubes, xyz_cubes_colors, axes[0], origins[i], scaling)
        
        for iter in range(1, len(axes)):
            display_func2(bottom_layers, bottom_layers_colors, axes[iter], origins[iter+2], scaling)
