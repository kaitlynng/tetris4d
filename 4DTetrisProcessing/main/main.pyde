<<<<<<< HEAD
import rotate4D
=======
from matmul import *
from rotate4D import *
>>>>>>> f8fdf7f8bd1e7c3e4d14b499376a43916ac152fc

worldSize = [5, 5, 5, 10] #x, y, z, u
screen_width = 1500
screen_height = 1000
scaling = 50
front_z = -500
#axes defined by hor, ver, dep
xyz_origin = [(screen_width/8)-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[1]/2)*scaling, 0]
xuz_origin = [(screen_width/8)*3-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]
xuy_origin = [(screen_width/8)*5-(worldSize[0]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]
yuz_origin = [(screen_width/8)*7-(worldSize[1]/2)*scaling, (screen_height/2)+(worldSize[2]/2)*scaling, 0]

#JUST FOR TEST, SORRY IF I FORGET TO REMOVE
shape = [[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]]

def setup():
    size(screen_width, screen_height, P3D)
    translate(0, 0, front_z)
    draw()

def draw():
    background(0)
    camera(width/2, 0, (height/2)/tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    drawBackground()

    pass

def keyPressed():
    switcher = {
        #Translations
        'q': p,
        'a': p,
        'w': p,
        's': p,
        'e': p,
        'd': p,
        #XU
        'r': rotate4D.rotate4D(shape, 3, 0),
        'f': rotate4D.rotate4D(shape, 3, 0),
        #YU
        't': rotate4D.rotate4D(shape, 4, 0),
        'g': rotate4D.rotate4D(shape, 4, 0),
        #ZU
        'y': rotate4D.rotate4D(shape, 5, 1),
        'h': rotate4D.rotate4D(shape, 5, 0),
        #XY
        'u': rotate4D.rotate4D(shape, 0, 1),
        'j': rotate4D.rotate4D(shape, 0, 0),
        #XZ
        'i': rotate4D.rotate4D(shape, 2, 1),
        'k': rotate4D.rotate4D(shape, 2, 0),
        #YZ
        'o': rotate4D.rotate4D(shape, 1, 1),
        'l': rotate4D.rotate4D(shape, 1, 0)
    }
    global shape
    shape = switcher.get(key)
    print(shape)

def p():
    return

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
    translate(origin[0], origin[1], origin[2])
    
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
    
            
