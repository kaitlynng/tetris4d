
import sys

import direct.directbase.DirectStart
from direct.interval.LerpInterval import LerpFunc
from panda3d.core import Texture, TextureStage

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
