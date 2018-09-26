#from direct.showbase.ShowBase import ShowBase
import sys

#from direct.task import Task
#from direct.actor.Actor import Actor
import direct.directbase.DirectStart
from direct.interval.LerpInterval import LerpFunc
from panda3d.core import Texture, TextureStage

#from math import pi, sin, cos
 
#class MyApp(ShowBase):
 
    #def __init__(self):
        #ShowBase.__init__(self)

base.setBackgroundColor(0.0, 0.0, 0.0)
base.disableMouse()

base.camera.setPos(0.0, -20.0, 10.0)
base.camera.lookAt(0.0, 0.0, 0.0)

root = render.attachNewNode("Root")
root.setPos(0.0, 0.0, 0.0)

modelCube = loader.loadModel("cube.egg")
cube = modelCube.copyTo(root)
cube.setH(2.0 ** i)

        
 
run()
