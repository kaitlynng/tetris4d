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
        display_func2(xyz_cubes, xyz_cubes_colors, axes[0], origins[0], scaling)
        
        for iter in range(1, len(axes)):
            display_func2(bottom_layers, bottom_layers_colors, axes[iter], origins[iter], scaling)
