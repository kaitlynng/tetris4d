from matmul import *
from rotate4D import *
import translate4D
import shapeFunctions

worldSize = [5, 5, 5, 10] #x, y, z, u
screen_width = 1800
screen_height = 1000
scaling = 50
front_z = -500

#axes defined by hor, ver, dep
xyz_origin = [(screen_width/8)-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[1]/2)*scaling, 0]
xuz_origin = [(screen_width/8)*3-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]
xuy_origin = [(screen_width/8)*5-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]
yuz_origin = [(screen_width/8)*7-(worldSize[1]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]

dropping = True

#JUST FOR TEST, SORRY IF I FORGET TO REMOVE
current_shape = [[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]]

def setup():
    size(screen_width, screen_height, P3D)
    translate(0, 0, front_z)
    draw()

def draw():
    background(0)
    camera(width/2, 0, (height/2)/tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    drawBackground()
    if dropping:
        initShape()
    current_shape.display()    

def keyPressed():
    global current_shape
    switcher = {
        #Translations
        'q': [0,1], 'a': [0,0], 
        'w': [1,1], 's': [1,0], 
        'e': [2,1], 'd': [2,0],
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
        'o': [1, 1], 'l': [1, 0]
    }
    if key in 'qawsed':
        current_shape.trans_shape(*switcher.get(key))
    if key in 'rftgyhujikol':
        current_shape.rot_shape(switcher.get(key))
    print(current_shape)

def initShape():
    global current_shape
    current_shape = Shape()
    dropping = False

def drawBackground():
    #xzy
    initGrid(xyz_origin, [worldSize[i] for i in [0, 1, 2]])
    #xzu
    initGrid(xuz_origin, [worldSize[i] for i in [0, 3, 2]])
    #xyu
    initGrid(xuy_origin, [worldSize[i] for i in [0, 3, 2]])
    #yuz
    initGrid(yuz_origin, [worldSize[i] for i in [1, 3, 2]])

def initGrid(origin, grid_size):
    #origin should be a list of three coordinates [hor, ver, dep]
    #size should be a list of three sizes [hor, ver, dep]
    stroke(255)
    noFill()
    
    pushMatrix()
    translate(*origin)
    
    #draw hor-ver plane
    beginShape()
    vertex(0, 0, 0)
    vertex(0, -scaling*grid_size[1], 0)
    vertex(scaling*grid_size[0], -scaling*grid_size[1], 0)
    vertex(scaling*grid_size[0], 0, 0)
    endShape()
    
    #draw yz plane
    beginShape()
    vertex(0, 0, 0)
    vertex(0, 0, scaling*grid_size[2])
    vertex(0, -scaling*grid_size[1], scaling*grid_size[2])
    vertex(0, -scaling*grid_size[1], 0)
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
    
