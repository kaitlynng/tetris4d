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
time_delta = 1
dropping = True
current_u = [0, 1, 0]

#change current_u

#variables for fixed blocks
current_shape = 0
bottom_layers = []
bottom_layers_colors = []
layer_num_list = [0]*world_size[3]


#variables for end screen
gameplay = 0
#0: start screen, 1: playing, 2: endgame, 3: pause game

#screen stuff
restart_button = widgets.Button('Press spacebar to play again, enter to return to start screen', [screen_width*0.6, screen_height*0.1, 0], [800, 50])
pause_list = widgets.Options(['Continue', 'End Game', 'Help Me'],
                             [screen_width*0.6, screen_height*0.32, 0],
                             [900, 80], 0)

helpme_u = 0
score = 0
clear_count = 0
#-----------------------------------------------------------------------------------------
# Screen functions
#-----------------------------------------------------------------------------------------

def startScreen():
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    textSize(80)
    textAlign(CENTER)
    fill(255,255,255)
    text("Difficulty: %.2f"%(2/time_delta), 0.5*screen_width, 0.3*screen_height, 0)
    textSize(20)
    textAlign(CENTER)
    fill(255,255,255)
    text("""spacebar to start; a,d to change difficulty (2.0 is recommended your for first game")
            Movement                                Rotation                       
                        Keys  Axis                Keys  Rotation plane      Keys  Rotation plane
                W, S  Z-axis              R, F  X-U plane              T, G  Y-U plane
                Q, E  Y-axis              Y, H  Z-U plane              U, J  X-Z plane
                A, D  X-axis              I, K  X-Y plane              O, L  Y-Z plane
        """, 0.5*screen_width, 0.06*screen_height, 0)
    
def playingScreen():
    global dropping, score
    #environment
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    if dropping:
        initShape()
    drawBackground()
    textSize(40)
    fill(210)
    textAlign(CENTER)
    text("Press spacebar to pause", 0.45*screen_width, 0.3*screen_height, 0)
    
    #updating
    current_shape.checkBounds(world_size)
    bottomlayers.checkClear(layer_num_list, world_size, bottom_layers, bottom_layers_colors, score)
    dropping = current_shape.checkStop(bottom_layers, bottom_layers_colors, dropping, layer_num_list)
    
    #display
    current_shape.displayShape(origins, scaling, current_u)
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, current_shape, origins, scaling, current_u)
    endGame()

def pauseScreen():
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, current_shape, origins, scaling, current_u)
    current_shape.displayShape(origins, scaling, current_u)
    textSize(120)
    textAlign(CENTER)
    fill(215)
    text("PAUSED", 0.95*screen_width, 0.2*screen_height, 0)
    pause_list.display()
    textSize(20)
    textAlign(CENTER)
    fill(255,255,255)
    text("""Spacebar to select. Choose 'Help Me' to clear an xyz space
            Movement                                Rotation                       
                        Keys  Axis                Keys  Rotation plane      Keys  Rotation plane
                W, S  Z-axis              R, F  X-U plane              T, G  Y-U plane
                Q, E  Y-axis              Y, H  Z-U plane              U, J  X-Z plane
                A, D  X-axis              I, K  X-Y plane              O, L  Y-Z plane
        """, 0.5*screen_width, 0.06*screen_height, 0)
        
def endScreen():
    #end screen
    global score
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, current_shape, origins, scaling, current_u)
    textSize(150)
    textAlign(CENTER, CENTER)
    fill(*[random.random()*255 for i in range(3)])
    textMode(SCREEN)
    text("You suck", 0.5*screen_width, 0.2*screen_height, 0)
    restart_button.display()
    textSize(35)
    fill(255)
    text("""
         Score:        {}
         Clear count:  {}
         Final score:  {}
         """.format(score, clear_count, score-clear_count), 0.82*screen_width, 0.22*screen_height, 0)

def helpMeScreen():
    background(0)
    camera(screen_width/2, height*5/6, (height/2)/tan(PI/6)*1.1, width/2, height*2/3, 0, 0, 1, 0)
    rotateX(-PI/5)
    drawBackground()
    bottomlayers.displayBottomLayers(bottom_layers, bottom_layers_colors, current_shape, origins, scaling, current_u)
    current_shape.displayShape(origins, scaling, current_u)
    textSize(120)
    textAlign(CENTER)
    fill(215)
    text("PAUSED", 0.95*screen_width, 0.2*screen_height, 0)
    textSize(40)
    fill(255)
    text("Clear XYZ-plane of U =    <  {}  >   Clear count: {}".format(helpme_u, clear_count), screen_width*0.6, screen_height*0.3, 0)
    textSize(20)
    textAlign(CENTER)
    fill(255,255,255)
    text("""Choose U with a and d. Spacebar to clear, Backspace/Delete to cancel.
            Movement                                Rotation                       
                        Keys  Axis                Keys  Rotation plane      Keys  Rotation plane
                W, S  Z-axis              R, F  X-U plane              T, G  Y-U plane
                Q, E  Y-axis              Y, H  Z-U plane              U, J  X-Z plane
                A, D  X-axis              I, K  X-Y plane              O, L  Y-Z plane
        """, 0.5*screen_width, 0.06*screen_height, 0)
    
screen_switcher = { 0: startScreen, 1: playingScreen, 2: endScreen, 3: pauseScreen, 4: helpMeScreen }

#-----------------------------------------------------------------------------------------
# Init game
#-----------------------------------------------------------------------------------------
def setup():
    size(screen_width, screen_height, P3D)
    translate(0,0,front_z)
    draw()

def draw():
    screen_switcher.get(gameplay)()

def keyPressed():
    #interactivity for moving shape
    global current_shape, current_u, helpme_u, gameplay
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
        #switch U
        'z': -1, 'x': 1
    #CALL LOCK AND UNLOCK HERE
            
    }
    if gameplay == 0:
        switcher = {
            'a': 0.1,
            'd': -0.1,
            ' ': 0
        }
        if str(key) in 'ad':
            change_difficulty(switcher.get(key))
        if str(key) in ' ':
            gameplay = 1
            return
    
    if gameplay in [1,2,3,4]:
        if key == 'z':
            if current_u[0] > 0:
                current_u = [value + shape_switcher.get(key) for value in current_u[0:2]]
        if key == 'x':
            if current_u[1] < world_size[3]:
                current_u = [value + shape_switcher.get(key) for value in current_u[0:2]]
    
    if gameplay == 1:
        if str(key) in 'qawsed':
            current_shape.transShape(*shape_switcher.get(key), bottom_layers=bottom_layers)
        if str(key) in 'rftgyhujikol':
            current_shape.rotShape(*shape_switcher.get(key), bottom_layers=bottom_layers, world_size=world_size)
        if key == ' ':
            gameplay = 3
            pause_list.select = 0
            return
    
    if gameplay == 2:
        if key == ' ':
            gameplay = 1
            resetGame()
            return
        if key == ENTER or key == RETURN:
            gameplay = 0 
            resetGame()
            return
    
    if gameplay == 3:
        if key == 'a':
            if pause_list.select > 0:
                pause_list.select -= 1
        if key == 'd':
            if pause_list.select < len(pause_list.items)-1:
                pause_list.select += 1
        if key == ' ':
            gameplay = (pause_list.select+1)*(pause_list.select in [0,1])+gameplay*(pause_list.select == 2)
            if pause_list.select == 2:
                gameplay = 4
                return
    
    if gameplay == 4:
        if key == 'a':
            if helpme_u > 0:
                helpme_u -= 1
        if key == 'd':
            if helpme_u < world_size[3]:
                helpme_u += 1
        if key == BACKSPACE or key == DELETE:
            gameplay = 3
        if key == ' ':
            helpMe()
            return
        
#-----------------------------------------------------------------------------------------
# Misc. functions
#-----------------------------------------------------------------------------------------
   
def change_difficulty(option):
    global time_delta
    time_delta += option

def initShape():
    #initialises new moving shape
    global current_shape, dropping, time_delta
    current_shape = shapeFunctions.Shape([int(world_size[0]/2), 0, int(world_size[2]/2), world_size[3]], time_delta)
    
    dropping = False

def endGame():
    #Condition for ending the game
    global gameplay,endscreen
    for coor in bottom_layers:
        if coor[3] == world_size[3]-1:
            gameplay = 2
            return

def resetGame():
    global bottom_layers, bottom_layers_colors, layer_num_list 
    global current_u, clear_count, score, dropping 
    bottom_layers = []
    bottom_layers_colors = []
    layer_num_list = [0]*world_size[3]
    current_u = [0, 1, 2]
    clear_count = 0
    score = 0
    dropping = True

def helpMe():
    global bottom_layers, bottom_layers_colors, clear_count
    temp_coor = []
    temp_colors = []
    for i in range(len(bottom_layers)):
        if bottom_layers[i][3] != helpme_u:
            temp_coor += [bottom_layers[i]]
            temp_colors += [bottom_layers_colors[i]]
    clear_count += 1*(len(temp_coor) < len(bottom_layers))
    bottom_layers = [coor for coor in temp_coor]
    bottom_layers_colors = [colors for colors in temp_colors]
            
            

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
    
