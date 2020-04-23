"""
Take samples of measures
"""

import numpy as np
from addict import Dict


def initialize(params):
    samples = Dict()

    samples.nsamples = params.nsamples
    samples.sampleInterval = params.ntimesteps / params.nsamples # for sample counter
    samples.sampleTime = params.timedelta * samples.sampleInterval # [ps] time interval for samples
    samples.sampleCountdown = 0
    samples.nsample = 0
    
    samples.time = np.zeros(samples.nsamples)
    samples.pressure = np.zeros(samples.nsamples)
    samples.temperature = np.zeros(samples.nsamples)
    samples.wallCollisions = np.zeros(samples.nsamples)
    samples.gasCollisions = np.zeros(samples.nsamples)
    samples.potentialEnergy = np.zeros(samples.nsamples)
    samples.kineticEnergy = np.zeros(samples.nsamples)
    samples.totalEnergy = np.zeros(samples.nsamples)
    # samples.concentration = np.zeros((samples.nsamples, nxSamples))
    # samples.temperatureDist = np.zeros((samples.nsamples, nxSamples))

    # # save initial velocity for histogram
    # if params.includeVelocityHistogram:
    #     vxInit = particles.velocity[:, 1]
    #     vInit = np.sqrt(np.sum(np.square(particles.velocity), axis=1))

    # return samples
    params.samples = samples


def update(params):
    measures = params.measures
    samples = params.samples

    # print(measures.wallCollisions)
    samples.time[samples.nsample] = params.currentTime
    samples.pressure[samples.nsample] = measures.pressure
    samples.temperature[samples.nsample] = measures.temperature
    samples.wallCollisions[samples.nsample] = measures.wallCollisions
    samples.gasCollisions[samples.nsample] = measures.gasCollisions
    samples.kineticEnergy[samples.nsample] = measures.kineticEnergy
    samples.potentialEnergy[samples.nsample] = measures.potentialEnergy
    samples.totalEnergy[samples.nsample] = measures.totalEnergy
    # # samples.concentration[samples.nsample,:] = np.transpose(measures.conc)
    # # samples.temperatureDist[samples.nsample,:] = measures.temp


    # clear cumulative variables
    #. should probably combine measure and sample - this is awkward
    measures.deltaMomentum = 0
    measures.wallCollisions = 0
    measures.gasCollisions = 0

