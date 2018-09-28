from matmul import *
from rotate4D import *
import translate4D
import shapeFunctions
import bottomlayers

world_size = [5, 5, 5, 10] #x, y, z, u
screen_width = 1400
screen_height = 1000
scaling = 50
front_z = -500

grid_stroke = 255
axes_name_size = 50
axes_name_color = 255
text_buffer = 20

#axes defined by hor, ver, dep
xyz1_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height/4)*3+(world_size[1]/2)*scaling, 0]
xyz2_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height/4)*2+(world_size[1]/2)*scaling, 0]
xyz3_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height/4)+(world_size[1]/2)*scaling, 0]
xuz_origin = [(screen_width/8)*3-(world_size[0]/2)*scaling, (screen_height/2)+(world_size[2]/2)*scaling, 0]
xuy_origin = [(screen_width/8)*5-(world_size[0]/2)*scaling, (screen_height/2)+(world_size[2]/2)*scaling, 0]
yuz_origin = [(screen_width/8)*7-(world_size[1]/2)*scaling, (screen_height/2)+(world_size[2]/2)*scaling, 0]
origins = [xyz1_origin, xyz2_origin, xyz3_origin, xuz_origin, xuy_origin, yuz_origin]
axes_names = [['X', 'Y', 'Z'], ['X', 'U', 'Z'], ['X', 'U', 'Y'], ['Y', 'U', 'Z']]
time_delta = 2

dropping = True
current_u = [0, 1, 2]

bottom_layers = []
bottom_layers_colors = []
layer_num_list = [0]*world_size[3]

def setup():
    size(screen_width, screen_height, P3D)
    translate(0, 0, front_z)
    draw()

def draw():
    global dropping
    background(0)
    camera(screen_width/2, 0, (height/2)/tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    drawBackground()
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, origins, scaling, current_u)
    if dropping:
        initShape()
        print("new shape")
    current_shape.checkBounds(world_size)
    bottomlayers.checkClear(layer_num_list, world_size, bottom_layers, bottom_layers_colors)
    current_shape.displayShape(origins, scaling, current_u)
    dropping = current_shape.checkStop(bottom_layers, bottom_layers_colors, dropping, layer_num_list)
    

def keyPressed():
    global current_shape, current_u
    switcher = {
        #Translations
        'q': [1,1], 'a': [0,-1], 
        'w': [2,-1], 's': [2,1], 
        'e': [1,-1], 'd': [0,1],
        #XU
        'r': [3, 1], 'f': [3, 0],
        #YU
        't': [4, 1], 'g': [4, 0],
        #ZU
        'y': [5, 1], 'h': [5, 0],
        #XY
        'u': [0, 1], 'j': [0, 0],
        #XZ
        'i': [2, 1], 'k': [2, 0],
        #YZ
        'o': [1, 1], 'l': [1, 0],
        #adjust u coordinate
        'z': -1, 'x': 1
    }
    if str(key) in 'qawsed':
        current_shape.transShape(*switcher.get(key), bottom_layers=bottom_layers)
    if str(key) in 'rftgyhujikol':
        current_shape.rotShape(*switcher.get(key), bottom_layers=bottom_layers)
    if str(key) in 'zx':
        current_u = [value + switcher.get(key) for value in current_u]

def initShape():
    global current_shape, dropping, time_delta
    current_shape = shapeFunctions.Shape([int(world_size[0]/2), world_size[1], int(world_size[2]/2), world_size[3]], time_delta)
    
    dropping = False


def drawBackground():
    #xzy
    initGrid(xyz1_origin, [world_size[i] for i in [0, 1, 2]])
    initGrid(xyz2_origin, [world_size[i] for i in [0, 1, 2]])
    initGrid(xyz3_origin, [world_size[i] for i in [0, 1, 2]])
    drawAxesName(xyz1_origin, [world_size[0], world_size[1]*3, world_size[2]], axes_names[0])

    #xzu
    initGrid(xuz_origin, [world_size[i] for i in [0, 3, 2]])
    drawAxesName(xuz_origin, [world_size[i] for i in [0, 3, 2]], axes_names[1])
    #xyu
    initGrid(xuy_origin, [world_size[i] for i in [0, 3, 2]])
    drawAxesName(xuy_origin, [world_size[i] for i in [0, 3, 2]], axes_names[2])

    #yuz
    initGrid(yuz_origin, [world_size[i] for i in [1, 3, 2]])
    drawAxesName(yuz_origin, [world_size[i] for i in [1, 3, 2]], axes_names[3])


def initGrid(origin, grid_size):
    #origin should be a list of three coordinates [hor, ver, dep]
    #size should be a list of three sizes [hor, ver, dep]
    
    stroke(grid_stroke)
    noFill()
    
    pushMatrix()
    translate(*origin)
    scale(1, -1, 1)
    
    #draw hor-ver plane
    beginShape()
    vertex(0, 0, 0)
    vertex(0, scaling*grid_size[1], 0)
    vertex(scaling*grid_size[0], scaling*grid_size[1], 0)
    vertex(scaling*grid_size[0], 0, 0)
    endShape()
    
    #draw yz plane
    beginShape()
    vertex(0, 0, 0)
    vertex(0, 0, scaling*grid_size[2])
    vertex(0, scaling*grid_size[1], scaling*grid_size[2])
    vertex(0, scaling*grid_size[1], 0)
    endShape()
    
    #draw xz grid
    pushMatrix()
    for n in range(grid_size[0]+1):
        line(0, 0, 0, 0, 0, scaling*grid_size[2])
        translate(scaling, 0, 0)
    popMatrix()
    pushMatrix()
    for n in range(grid_size[2]+1):
        line(0, 0, 0, scaling*grid_size[0], 0, 0)
        translate(0, 0, scaling)
    popMatrix()
    
    popMatrix()

def drawAxesName(origin, grid_size, axes_name):
    textSize(axes_name_size)
    fill(axes_name_color)
    textAlign(CENTER)
    #write XYZ
    
    #write XUZ
    pushMatrix()
    translate(*origin)
    text(axes_name[0], grid_size[0]/2*scaling, axes_name_size/2+text_buffer, grid_size[2]*scaling)
    text(axes_name[1], grid_size[0]*scaling+axes_name_size/2+text_buffer, -grid_size[1]/2*scaling, 0)
    text(axes_name[2], grid_size[0]*scaling+axes_name_size/2+text_buffer, 0, grid_size[2]/2*scaling)
    popMatrix()
    
