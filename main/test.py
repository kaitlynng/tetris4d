import sys
 
import direct.directbase.DirectStart
from direct.interval.LerpInterval import LerpFunc
from panda3d.core import Texture, TextureStage
 
base.setBackgroundColor(0.0, 0.0, 0.0)
base.disableMouse()
 
base.camLens.setNearFar(1.0, 50.0)
base.camLens.setFov(45.0)
 
camera.setPos(0.0, -20.0, 10.0)
camera.lookAt(0.0, 0.0, 0.0)
 
root = render.attachNewNode("Root")
root.setPos(0.0, 0.0, 0.0)

#THIS IS THE LINE THAT GIVES THE ERROR
modelCube = loader.loadModel("cube.egg")

base.run()
