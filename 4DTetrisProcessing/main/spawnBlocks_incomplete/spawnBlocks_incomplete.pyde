def spawnblock() :
    #FILL IN
    defaultSpawnCoord = 
    
    4BlockShapes = [[[0,0,0,0],[1,0,0,0],[2,0,0,0],[3,0,0,0]],
                   [[0,0,0,0],[1,0,0,0],[2,0,0,0],[2,0,1,0]],
                   [[0,0,0,0],[1,0,0,0],[1,0,1,0],[2,0,1,0]],
                   [[0,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,0,0]],
                   [[0,0,0,0],[1,0,0,0],[2,0,0,0],[1,1,0,0]],
                   [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]],
                   [[0,0,0,0],[0,1,0,0],[0,1,1,0],[1,1,1,0]]]
    
    index = int(random(len(4BlockShapes)))
    spawnCoords = [4BlockShapes[index][i] + defaultSpawnCoord[i] for i in range(len(defaultSpawnCoord))]
    
    #STILL HAVE TO DRAW BLOCKS AND ADD PLAYER CONTROL
