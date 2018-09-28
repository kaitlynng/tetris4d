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

def checkClear(layer_num_list, world_size, bottom_layers, bottom_layers_colors):
    layermax = world_size[0]*world_size[1]*world_size[2]
    for iter in range(len(layer_num_list)):
        if layer_num_list[iter] >= layermax:
            for i in range(iter,len(layer_num_list)-1):
                layer_num_list[i] = layer_num_list[i+1]
            layer_num_list[len(layer_num_list)-1] = 0
            print(bottom_layers)
            remove_list = []
            for i in bottom_layers:
                if i[3] == iter:
                    remove_list.append(i)
                if i[3] > iter:
                    i[3] -= 1
            for i in remove_list:
                bottom_layers_colors.remove(bottom_layers_colors[bottom_layers.index(i)])
                bottom_layers.remove(i)
                


            
