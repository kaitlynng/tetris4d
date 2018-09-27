print("Friendship ended with Panda3D")

def setup():
    size(800, 1000, P3D)
    draw()
    
def draw():
    background(0)
    lights()
    pushMatrix()
    translate(width/2, height/2, 0)
    stroke(150)
    box(100)
    
    translate(0, 200/2, 0)
    box(100)
    popMatrix()
    camera(mouseX, height/2, (height/2)/tan(PI/6), width/2, height/2, 0, 0, 1, 0)
