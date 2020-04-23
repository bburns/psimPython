"""
psim
Particle Simulator

All variables are stored in a namespace variable, 'params' -
so can pass data around easily between functions.
"""

import particles
import box
import views
import sample
import expect
import measure
import profile
import integrate


def initialize(params):
    """
    Initialize the experiment
    """
    # add more info to params namespace
    params.ntimesteps = int(params.duration / params.timedelta) # total number of time steps during run    
    box.initialize(params) # get box dimensions etc
    particles.initialize(params) # initialize particle positions and velocities
    sample.initialize(params) # initialize sample counters and arrays
    measure.initialize(params) # initialize measures
    expect.initialize(params) # calculate expected values
    views.initialize(params) # display initial messages, initialize charts
    profile.initialize(params) # initialize the profile to track cpu time


def run(params):
    """
    Run the experiment
    """
    samples = params.samples
    for params.ntimestep in range(0, params.ntimesteps):
        params.currentTime = params.ntimestep * params.timedelta
        particles.update(params) # get potential energy
        if samples.sampleCountdown == 0:
            measure.update(params) # measure system properties
            sample.update(params) # record samples
            views.update(params)  # update views
            samples.nsample += 1
            samples.sampleCountdown = samples.sampleInterval
        integrate.update(params) # integrate equations of motion, handle collisions
        samples.sampleCountdown -= 1


def finalize(params):
    """
    Finish the experiment
    """
    measure.finalize(params)
    views.finalize(params)


def main():
    """
    Import and run an experiment
    """

    # import experimental parameters from file specified on command line, 
    # or a default experiment.
    from params import params 

    initialize(params)
    run(params)
    finalize(params)


# if this file is being run as the main module, eg with `python psim`,
# then call the main() function.
# see https://stackoverflow.com/questions/4041238/why-use-def-main
if __name__ == '__main__':
    main()
