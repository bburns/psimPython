"""
Handle visualizations for experiments
"""

import matplotlib.pyplot as plt # charting library
# import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D # 3d plots


fig = None
ax = None


def initialize(sim):

    plt.ion() # interactive mode on
    global fig, ax
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') # first param is nrows ncols index
    ax.set_xlabel('x-axis (A)')
    ax.set_ylabel('y-axis (A)')
    ax.set_zlabel('z-axis (A)')
    # ax.axis('equal')
    
    # define 3d shape
    # Define the 8 vertices of the unit cube, then define the 6 faces of the box, 
    # then scale the vertices by the box dimensions.
    # unitCubeVertices = [0 0 0 1 0 0 1 1 0 0 1 0 0 0 1 1 0 1 1 1 1 0 1 1] 
    # boxFaces = [1 2 6 5 2 3 7 6 3 4 8 7 4 1 5 8 1 2 3 4 5 6 7 8]
    # boxVertices = unitCubeVertices * box.matrix
    
    # draw particles in 3d
    for species in sim.species:
        # hPlot[iSpecies] = plot3(particles.position(iRange,1), particles.position(iRange,2), particles.position[iRange, 3], markerStyle) # x,y,z
        # markerStyle = '.' + species.color # eg '.r'
        # markerSize = species.radius * 10
        # set(hPlot[iSpecies], 'MarkerSize', markerSize)
        # hold on
        iRange = species.iRange
        xs = sim.particles.position[iRange, 0]
        ys = sim.particles.position[iRange, 1]
        zs = sim.particles.position[iRange, 2]
        color = species.color
        # ax.scatter(xs, ys, zs, color=color, marker=markerSize)
        ax.scatter(xs, ys, zs, color=color)
    
    # # Create 3d container object for display
    # hContainer = patch('Vertices',boxVertices, 'Faces',boxFaces, 'FaceColor','blue')
    # alpha(0.25) # make transparent!
    
    # # Set axis lengths
    # axisMin = 0
    # axis([axisMin boxSize[1] axisMin boxSize[2] axisMin boxSize[3]])
    # axis equal
    # axis vis3d # freezes aspect ratio properties to enable rotation of 3-D objects
    # grid on
    
    # # Show 3d figure
    # view(3)
    # camproj perspective
    # rotate3d on # turn on mouse-based 3-D rotation
    # set(gca,'CameraViewAngleMode','manual') # prevents graph from being resized as rotated
    # drawnow

    ax.set_proj_type('persp')
    ax.set_xlim3d(0, sim.boxsize[0])
    ax.set_ylim3d(0, sim.boxsize[1])
    ax.set_zlim3d(0, sim.boxsize[2])

    # set_axes_equal(ax)
    
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    # fig.show()
    # plt.show()

def update(sim):
    # tic()
    # for species in  sim.species:
    #     iRange = species.iRange
    #     # update 3d display
    #     # set(hPlot[iSpecies], 'XData',particles.position[iRange, 1], 'YData',particles.position[iRange, 2], 'ZData',particles.position[iRange, 3])
    # # drawnow
    for species in sim.species:
        # hPlot[iSpecies] = plot3(particles.position(iRange,1), particles.position(iRange,2), particles.position[iRange, 3], markerStyle) # x,y,z
        # markerStyle = '.' + species.color # eg '.r'
        # markerSize = species.radius * 10
        # set(hPlot[iSpecies], 'MarkerSize', markerSize)
        # hold on
        iRange = species.iRange
        xs = sim.particles.position[iRange, 0]
        ys = sim.particles.position[iRange, 1]
        zs = sim.particles.position[iRange, 2]
        color = species.color
        # ax.scatter(xs, ys, zs, color=color, marker=markerSize)
        ax.scatter(xs, ys, zs, color=color)
    plt.pause(0.1) # need this for chart to update - plot data and run gui event loop


    # timeDisplay = timeDisplay + toc()

def finalize(sim):
    plt.ioff() # interactive mode off - need this to leave plots on
    # fig.savefig('foo.png')
    plt.show()

