"""
psim
Particle Simulator

All variables are stored in a namespace variable, 'sim' -
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


def initialize(sim):
    """
    Initialize the experiment
    """
    # add more info to sim namespace
    sim.ntimesteps = int(sim.duration / sim.timedelta) # total number of time steps during run    
    box.initialize(sim) # get box dimensions etc
    particles.initialize(sim) # initialize particle positions and velocities
    sampler.initialize(sim) # initialize sample counters and arrays
    measurer.initialize(sim) # initialize measures
    expecter.initialize(sim) # calculate expected values
    views.initialize(sim) # display initial messages, initialize charts
    profiler.initialize(sim) # initialize the profiler to track cpu time


def run(sim):
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


def finalize(sim):
    """
    Finish the experiment
    """
    measurer.finalize(sim)
    views.finalize(sim)


def main():
    """
    Import and run an experiment
    """

    # import experimental parameters from file specified on command line, 
    # or a default experiment.
    from params import params 

    sim = params

    initialize(sim)
    run(sim)
    finalize(sim)


# if this file is being run as the main module, eg with `python psim`,
# then call the main() function.
# see https://stackoverflow.com/questions/4041238/why-use-def-main
if __name__ == '__main__':
    main()
