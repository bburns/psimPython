"""
psim
Particle Simulator
"""

# from params import params # the experiment parameters
# import experiment

# experiment.initialize(params)
# experiment.run()
# experiment.finalize()

"""
Run an experiment

All variables are stored in a module-level namespace variable, 'sim' -
so can pass data around easily between functions.
It's a Dict object from the 'addict' library, which lets you access values like
foo.bar instead of foo['bar']. 
"""

import particles
import box
import views
import sampler
import expecter
import measurer
import profiler
import integrator


#. call this globals
#. define what's in it
#. make some kind of struct?
sim = None # namespace with particle arrays etc


def initialize(params):
    """
    Initialize the experiment
    """
    # get parameters into namespace
    global sim
    sim = params

    # now add more info to namespace
    sim.ntimesteps = int(sim.duration / sim.timedelta) # total number of time steps during run    
    box.initialize(sim) # get box dimensions etc
    particles.initialize(sim) # initialize particle positions and velocities
    sampler.initialize(sim) # initialize sample counters and arrays
    measurer.initialize(sim) # initialize measures
    expecter.initialize(sim) # calculate expected values
    views.initialize(sim) # display initial messages, initialize charts
    profiler.initialize(sim) # initialize the profiler to track cpu time


def run():
    """
    Run the experiment
    """
    samples = sim.samples
    for sim.ntimestep in range(0, sim.ntimesteps):
        sim.currentTime = sim.ntimestep * sim.timedelta
        particles.update(sim) # get potential energy
        if samples.sampleCountdown == 0:
            measurer.update(sim) # measure system properties
            sampler.update(sim) # record samples
            views.update(sim)  # update views
            samples.nsample += 1
            samples.sampleCountdown = samples.sampleInterval
        integrator.update(sim) # integrate equations of motion, handle collisions
        samples.sampleCountdown -= 1


def finalize():
    """
    Finish the experiment
    """
    measurer.finalize(sim)
    views.finalize(sim)



if __name__ == '__main__':
    from params import params
    initialize(params)
    run()
    finalize()
