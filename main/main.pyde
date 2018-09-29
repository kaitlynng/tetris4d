from matmul import *
from rotate4D import *
import random
import time

import translate4D
import shapeFunctions
import bottomlayers
import widgets

#-----------------------------------------------------------------------------------------
# Init variables
#-----------------------------------------------------------------------------------------

#environment variables
world_size = [5, 5, 5, 10] #x, y, z, u
screen_width = 1400
screen_height = 1000
scaling = 50
front_z = -500

#drawing
grid_stroke = 255
axes_name_size = 50
axes_name_color = 255
text_buffer = 20

#axes defined by hor, ver, dep
xyz1_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height*20/24)+(world_size[1]/2)*scaling, 0]
xyz2_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height*13/24)+(world_size[1]/2)*scaling, 0]
xyz3_origin = [(screen_width/8)-(world_size[0]/2)*scaling, (screen_height*6/24)+(world_size[1]/2)*scaling, 0]
xuz_origin = [(screen_width/8)*3-(world_size[0]/2)*scaling, (screen_height*3/4)+(world_size[2]/2)*scaling, 0]
xuy_origin = [(screen_width/8)*5-(world_size[0]/2)*scaling, (screen_height*3/4)+(world_size[2]/2)*scaling, 0]
yuz_origin = [(screen_width/8)*7-(world_size[1]/2)*scaling, (screen_height*3/4)+(world_size[2]/2)*scaling, 0]
origins = [xyz1_origin, xyz2_origin, xyz3_origin, xuz_origin, xuy_origin, yuz_origin]
axes_names = [['X', 'Y', 'Z'], ['X', 'U', 'Z'], ['X', 'U', 'Y'], ['Y', 'U', 'Z']]

#variables for updating
time_delta = 0.1
dropping = True
current_u = [0, 1, 2]

#variables for fixed blocks
bottom_layers = []
bottom_layers_colors = []
layer_num_list = [0]*world_size[3]

gameplay = 0
#0: start screen, 1: playing, 2: endgame, 3: pause game

#screen stuff
start_button = widgets.Button('PRESS SPACEBAR TO START', [screen_width/2, screen_height/2, 0], [600, 80])
restart_button = widgets.Button('Press spacebar to play again, enter to return to start screen', [screen_width/2+200, 100, 0], [800, 50])
pause_list = widgets.Options(['Continue', 'End Game', 'Help Me'],
                             [200, screen_height/2 + 100, 0],
                             [400, 300], 0)
help_me = False

#-----------------------------------------------------------------------------------------
# Screen functions
#-----------------------------------------------------------------------------------------

def startScreen():
    background(0)
    textAlign(CENTER, CENTER)
    textSize(100)
    fill(255)
    text("Tetris 4D", screen_width/2, screen_height/4, 0)
    start_button.display()

def playingScreen():
    global dropping
    #environment
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    
    #updating
    if dropping:
        initShape()
    current_shape.checkBounds(world_size)
    bottomlayers.checkClear(layer_num_list, world_size, bottom_layers, bottom_layers_colors)
    dropping = current_shape.checkStop(bottom_layers, bottom_layers_colors, dropping, layer_num_list)
    
    #display
    current_shape.displayShape(origins, scaling, current_u)
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, origins, scaling, current_u)
    endGame()

def pauseScreen():
    background(0)
    textAlign(CENTER, CENTER)
    textSize(100)
    fill(255)
    textMode(SCREEN)
    text("GAME PAUSED", screen_width/2, screen_height/4, 0)
    pause_list.display()
        
def endScreen():
    #end screen
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, origins, scaling, current_u)
    textSize(200)
    textAlign(CENTER, CENTER)
    fill(*[random.random()*255 for i in range(3)])
    textMode(SCREEN)
    text("You suck", screen_width-500, 200, 0)
    restart_button.display()

screen_switcher = { 0: startScreen, 1: playingScreen, 2: endScreen, 3: pauseScreen }

#-----------------------------------------------------------------------------------------
# Init game
#-----------------------------------------------------------------------------------------

def setup():
    size(screen_width, screen_height, P3D)
    translate(0, 0, front_z)
    draw()

def draw():
    screen_switcher.get(gameplay)()

def keyPressed():
    #interactivity for moving shape
    global current_shape, current_u, gameplay
    shape_switcher = {
        #Translations
        'q': [1,1], 'a': [0,-1], 
        'w': [2,-1], 's': [2,1], 
        'e': [1,-1], 'd': [0,1],
        #Rotations
        #XU
        'r': [3, 1], 'f': [3, 0],
        #YU
        't': [4, 1], 'g': [4, 0],
        #ZU
        'y': [5, 1], 'h': [5, 0],
        #XY
        'i': [0, 1], 'k': [0, 0],
        #XZ
        'u': [2, 1], 'j': [2, 0],
        #YZ
        'o': [1, 1], 'l': [1, 0],
        #Adjust U coordinate
        'z': -1, 'x': 1
    }
    if gameplay == 0:
        if key == ' ':
            gameplay = 1
            return
    
    if gameplay == 1:
        if str(key) in 'qawsed':
            current_shape.transShape(*shape_switcher.get(key), bottom_layers=bottom_layers)
        if str(key) in 'rftgyhujikol':
            current_shape.rotShape(*shape_switcher.get(key), bottom_layers=bottom_layers, world_size=world_size)
        if str(key) in 'z':
            if current_u[0] > 0:
                current_u = [value + shape_switcher.get(key) for value in current_u]
                print(current_u)
        if str(key) in 'x':
            if current_u[2] < world_size[3]:
                current_u = [value + shape_switcher.get(key) for value in current_u]
        if key == ' ':
            gameplay = 3
            pause_list.select = 0
            return
    
    if gameplay == 2:
        if key == ' ':
            gameplay = 1
            resetGame()
        if key == ENTER or key == RETURN:
            gameplay = 0 
            resetGame()
            return
    
    if gameplay == 3:
        if key == CODED:
            if keyCode == DOWN:
                pause_list.select += 1
            if keyCode == UP:
                pause_list.select -= 1
            if pause_list.select < 0:
                pause_list.select = 0
            if pause_list.select >= len(pause_list.items):
                pause_list.select = len(pause_list.items)-1
        if key == ENTER or key == RETURN:
            gameplay = (pause_list.select+1)*(pause_list.select in [0,1])+gameplay*(pause_list.select == 2)
            if key == 2:
                help_me = True

#-----------------------------------------------------------------------------------------
# Misc. functions
#-----------------------------------------------------------------------------------------

def initShape():
    #initialises new moving shape
    global current_shape, dropping, time_delta
    current_shape = shapeFunctions.Shape([int(world_size[0]/2), world_size[1], int(world_size[2]/2), world_size[3]], time_delta)
    
    dropping = False

def endGame():
    #Condition for ending the game
    global gameplay
    for coor in bottom_layers:
        if coor[3] == world_size[3]-1:
            gameplay = 2
            return

def resetGame():
    global bottom_layers, bottom_layers_colors, current_u
    bottom_layers = []
    bottom_layers_colors = []
    layer_num_list = [0]*world_size[3]
    current_u = [0, 1, 2]

#-----------------------------------------------------------------------------------------
# Draw Axes
#-----------------------------------------------------------------------------------------

def drawBackground():
    #Draws grids and labels
    global current_u
    #xzy
    initGrid(xyz1_origin, [world_size[i] for i in [0, 1, 2]])
    initGrid(xyz2_origin, [world_size[i] for i in [0, 1, 2]])
    initGrid(xyz3_origin, [world_size[i] for i in [0, 1, 2]])
    drawAxesName(xyz1_origin, [world_size[0], world_size[1]*3, world_size[2]], axes_names[0])
    drawUValues([xyz1_origin, xyz2_origin, xyz3_origin], [world_size[0], world_size[1], world_size[2]], current_u)

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
    #itialises grids
    
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
    #draws axe labels
    
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
    
def drawUValues(origins, grid_size, current_u):
    #draw U-value labels
    
    textSize(axes_name_size)
    fill(axes_name_color)
    textAlign(CENTER)
    
    for i in range(len(origins)):
        pushMatrix()
        translate(*origins[i])
        text("U = %d"%current_u[i], -grid_size[0]*scaling+axes_name_size/2+text_buffer, 0, grid_size[2]/2*scaling)
        popMatrix()
    
