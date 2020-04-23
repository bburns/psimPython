"""
Handle charting output for experiments
"""

import matplotlib.pyplot as plt # charting library
# from mpl_toolkits.mplot3d import Axes3D # 3d plots

# declare matplotlib figure and charts
fig = None
ax1 = None
ax2 = None
ax3 = None
ax4 = None
ax5 = None
h1 = None
h2 = None
h3 = None
h4 = None
h5a = h5b = h5c = None


def initialize(sim):
    expected = sim.expected

    plt.ion() # interactive mode on

    global fig
    global ax1, ax2, ax3, ax4, ax5
    global h1, h2, h3, h4, h5a, h5b, h5c

    # ScreenSize is a four-element vector: [left, bottom, width, height]:
    # screensize = get(0,'ScreenSize')
    # pos = [20 40 screensize(3)*.8 screensize(4)*.8]
    # figure('position', pos)

    fig = plt.figure()

    nrows = 2
    ncols = 3

    ax1 = fig.add_subplot(nrows, ncols, 1)
    ax1.set_ylabel('Pressure (atm)')
    ax1.set_xlabel('Time (ps)')
    ax1.axhline(expected.pressure, color='g')
    h1, = ax1.plot([], [], color='r')

    ax2 = fig.add_subplot(nrows, ncols, 2)
    ax2.set_ylabel('Temperature (K)')
    ax2.set_xlabel('Time (ps)')
    ax2.axhline(expected.temperature, color='g')
    h2, = ax2.plot([], [], color='r')

    ax3 = fig.add_subplot(nrows, ncols, 4)
    ax3.set_ylabel('Wall collisions')
    ax3.set_xlabel('Time (ps)')
    # ax3.axhline(expected.wallCollisions, color='g')
    h3, = ax3.plot([], [], color='r')

    ax4 = fig.add_subplot(nrows, ncols, 5)
    ax4.set_ylabel('Gas collisions')
    ax4.set_xlabel('Time (ps)')
    # ax4.axhline(expectedGasCollisions, color='g')
    h4, = ax4.plot([], [], color='r')

    ax5 = fig.add_subplot(nrows, ncols, 3)
    ax5.set_ylabel('Energy (Moules)')
    ax5.set_xlabel('Time (ps)')
    # ax5.set_legend('ke','pe','e')
    h5a, = ax5.plot([], [], color='r')
    h5b, = ax5.plot([], [], color='b')
    h5c, = ax5.plot([], [], color='purple')


    plt.tight_layout() # optimize spacing between plots


def update(sim):
    
    samples = sim.samples
    expected = sim.expected

    iRange = slice(0, samples.nsample+1)

    h1.set_data(samples.time[iRange], samples.pressure[iRange])
    ax1.relim()
    ax1.autoscale_view()

    h2.set_data(samples.time[iRange], samples.temperature[iRange])
    ax2.relim()
    ax2.autoscale_view()

    h3.set_data(samples.time[iRange], samples.wallCollisions[iRange])
    ax3.relim()
    ax3.autoscale_view()

    h4.set_data(samples.time[iRange], samples.gasCollisions[iRange])
    ax4.relim()
    ax4.autoscale_view()

    # ax5.plot(dataTime, dataKineticEnergy,'r')
    # ax5.plot(dataTime, dataPotentialEnergy,'b')
    # ax5.plot(dataTime, dataKineticEnergy + dataPotentialEnergy,'p')
    h5a.set_data(samples.time[iRange], samples.kineticEnergy[iRange])
    h5b.set_data(samples.time[iRange], samples.potentialEnergy[iRange])
    h5c.set_data(samples.time[iRange], samples.totalEnergy[iRange])
    ax5.relim()
    ax5.autoscale_view()


    # ax = fig.add_subplot(337)
    # ax.surf(xRange,timeRange,dataConcentration)
    # ax.set_xlabel('x (A)')
    # ax.set_ylabel('time (ps)')
    # ax.set_zlabel('conc')

    # ax = fig.add_subplot(338)
    # ax.surf(xRange,timeRange,dataTemperatureDist)
    # ax.set_xlabel('x (A)')
    # ax.set_ylabel('time (ps)')
    # ax.set_zlabel('temp (K)')

    # camproj(perspective)
    # rotate3d(on) # turn on mouse-based 3-D rotation


    # #-----------------------------------------------------------------------------------
    # # Compare velocity distributions
    # #-----------------------------------------------------------------------------------
    # if includeVelocityHistogram:
    #     figure
    #     x = 18
        
    #     subplot 221
    #     hist(vxInit, x)
    #     ax.set_title('vx init')
        
    #     subplot 223
    #     hist(vInit, x)
    #     ax.set_title('v init')
        
    #     subplot 222
    #     hist(vxFinal, x)
    #     ax.set_title('vx final')
    #     # plot against maxwell-boltzmann velocity distribution
    #     hold on
    #     plot(s2,expectedSpeedDistribution1d)
        
    #     subplot 224
    #     hist(vFinal, x)
    #     ax.set_title('v final')
    #     # plot against maxwell-boltzmann velocity distribution
    #     hold on
    #     plot(s,expectedSpeedDistribution)
        
    #     # change color
    #     h = findobj(gcf,'Type','patch')
    #     set(h,'FaceColor','g','EdgeColor','w')

    # fig.show()
    fig.canvas.draw()
    plt.pause(0.1) # need this for chart to update - plot data and run gui event loop

def finalize(sim):
    plt.ioff() # interactive mode off - need this to leave plots on
    plt.show()
