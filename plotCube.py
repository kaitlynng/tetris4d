import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig, ax = plt.subplots(2, 2, subplot_kw=dict(projection='3d'))

def getCubeDef(corner):
    #corner type: np array
    corner_x, corner_y, corner_z = np.zeros(corner.shape)
    corner = corner-0.5
    corner_x += corner[:]
    corner_y += corner[:]
    corner_z += corner[:]
    corner_x[0], corner_y[1], corner_z[2] = corner_x[0]+1, corner_y[1]+1, corner_z[2]+1
    #function returns list of np arrays
    return [corner, corner_x, corner_y, corner_z]

def plotCube(cube_definition_array, subplot):
# equate points with cube_definition_array without assignment
    points = []
    points += cube_definition_array

#define the three axis vectors (x vector, y vector, z vector)
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

# add the rest of the points in the cube
    points += [cube_definition_array[0] + vectors[0] + vectors[1]] #corner + xvec + yvec
    points += [cube_definition_array[0] + vectors[0] + vectors[2]] #corner + xvec + zvec
    points += [cube_definition_array[0] + vectors[1] + vectors[2]] #coner + yvec + zvec
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]] #furthest point

#points are: (0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1), (1,1,1)

#convert points to np array (points were original np arrays in lists to facilitate adding)
    points = np.array(points)

#edges give the wireframe to pass to Poly3DCollection to form faces
    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]

#form faces using poly3DCollection
    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor((0,0,1,0.1))

    subplot.add_collection3d(faces)

    # Plot the points themselves to scale the axes, probably not needed actually
    subplot.scatter(points[:,0], points[:,1], points[:,2], s=0)

def adjustAxis(X, Y, Z, subplot):
    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
    # Comment or uncomment following both lines to test the fake bounding box:
    for xb, yb, zb in zip(Xb, Yb, Zb):
        subplot.plot([xb], [yb], [zb], 'w')

def plot3D(shape3D_dat, subplot):
    #shape_3D_dat type: np array
    for item in range(0, shape3D_dat.shape[0]):
        plotCube(getCubeDef(shape3D_dat[item]), subplot)
    [X, Y, Z] = np.transpose(shape3D_dat)
    adjustAxis(X, Y, Z, subplot)

def plotShape(shape4D_dat):
    #hape4D_dat type: no matrix of coordinates

    #plot xyz
    plot3D(shape4D_dat[:, :3], ax[0,0])
    ax[0,0].set_title('XYZ axis')
    ax[0,0].set_xlabel('X')
    ax[0,0].set_ylabel('Y')
    ax[0,0].set_zlabel('Z')

    #plot yzu
    plot3D(shape4D_dat[:, 1:], ax[0,1])
    ax[0,1].set_title('YZU axis')
    ax[0,1].set_xlabel('Y')
    ax[0,1].set_ylabel('Z')
    ax[0,1].set_zlabel('U')

    #plot xzu
    plot3D(shape4D_dat[:, [0,2,3]], ax[1,0])
    ax[1,0].set_title('XZU axis')
    ax[1,0].set_xlabel('X')
    ax[1,0].set_ylabel('Z')
    ax[1,0].set_zlabel('U')

    #plot xyu
    plot3D(shape4D_dat[:, [0,1,3]], ax[1,1])
    ax[1,1].set_title('XYU axis')
    ax[1,1].set_xlabel('X')
    ax[1,1].set_ylabel('Y')
    ax[1,1].set_zlabel('U')

    plt.show()
