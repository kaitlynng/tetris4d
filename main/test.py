import sys

import direct.directbase.DirectStart
from direct.interval.LerpInterval import LerpFunc
from panda3d.core import Texture, TextureStage

base.setBackgroundColor(0.0, 0.0, 0.0)
base.disableMouse()

base.camLens.setNvearFar(1.0, 50.0)
base.camLens.setFov(45.0)

camera.setPos(0.0, -20.0, 10.0)
camera.lookAt(0.0, 0.0, 0.0)

root = render.attachNewNode("Root")
root.setPos(0.0, 0.0, 0.0)

#THIS IS THE LINE THAT GIVES THE ERROR
modelCube = loader.loadModel("cube.egg")

cubes = []
for x in [-3.0, 0.0, 3.0]:
    cube = modelCube.copyTo(root)
    cube.setPos(x, 0.0, 0.0)
    cubes += [ cube ]

base.accept("escape", sys.exit)

base.accept("o", base.oobe)

def animate(t):
    for i in range(len(cubes)):
        cubes[i].setH(t * (2.0 ** i))

interval = LerpFunc(animate, 5.0, 0.0, 360.0)

base.accept("i", interval.start)

def move(x, y, z):
    root.setX(root.getX() + x)
    root.setY(root.getY() + y)
    root.setZ(root.getZ() + z)

base.accept("d", move, [1.0, 0.0, 0.0])
base.accept("a", move, [-1.0, 0.0, 0.0])
base.accept("w", move, [0.0, 1.0, 0.0])
base.accept("s", move, [0.0, -1.0, 0.0])
base.accept("e", move, [0.0, 0.0, 1.0])
base.accept("q", move, [0.0, 0.0, -1.0])

run()
