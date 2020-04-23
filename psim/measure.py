import numpy as np
from addict import Dict
from constants import *


def initialize(params):
    measures = Dict()
    # initialize cumulative variables
    measures.deltaMomentum = 0
    measures.wallCollisions = 0
    measures.gasCollisions = 0
    params.measures = measures


def update(params):
    particles = params.particles
    measures = params.measures
    samples = params.samples

    # import random
    # measures.pressure = random.random()

    # Calculate various properties based on the particle distribution and velocity. 
    # Note: sampleTime = amount of time elapsed since last sample was taken [ps]
    # PlanarPressure (atm) ie specify plane, get array of pressure points for graphical output
    # pressure [atm] is averaged over all surfaces

    # tic()
    # measures.pressure = measures.deltaMomentum / params.box.area / samples.sampleTime * pascalsPerMascal * atmospheresPerPascal # [atm]
    measures.pressure = measures.deltaMomentum / params.box.area / samples.sampleTime * atmospheresPerMascal # [atm]
    # numericDensity = self.nparticles / self.box.volume # [Atoms/A^3]
    # # speedSquared = sum(particles.velocity .* particles.velocity, 2) # v squared = (vx)^2 + (vy)^2 + (vz)^2    [array, summed across rows]
    speedSquared = np.sum(np.square(particles.velocity), axis=1) # v squared = (vx)^2 + (vy)^2 + (vz)^2    [array, summed across rows]
    measures.potentialEnergy = np.sum(particles.potential) # [Moules]
    measures.kineticEnergy = 0.5 * np.dot(speedSquared, particles.mass) # [Moules] # sum of 0.5 * particles.mass[i] * speedSquared[i]
    measures.temperature = 2.0 / 3.0 * measures.kineticEnergy / kb / params.nparticles # [K] . dif for diatomic gas?
    measures.totalEnergy = measures.kineticEnergy + measures.potentialEnergy # [Moules]
    # print(measures)

    # # get concentration distribution of species 1
    # conc = histc(particles.position(species(1).jRange,1),xRange)

    # # get temperature distribution of all species
    # # bin is an array that tells you which bin each particle went into (0 to nxSamples)
    # ke = zeros(nxSamples,1)
    # count = zeros(nxSamples,1)
    # for i=1:self.nparticles
    #     nBin = floor(particles.position[i,0]/boxSize[1] * nxSamples) + 1 # 1 to nxSamples
    #     if nBin < 1 
    #         nBin = 1
    #     end
    #     if nBin > nxSamples
    #         nBin = nxSamples
    #     end
    #     ke(nBin) = ke(nBin) + 0.5 * particles.mass[i] * speedSquared[i]
    #     count(nBin) = count(nBin) + 1
    # end
    # for i = 1:nxSamples
    #     temp[i] = 2.0 / 3.0 * ke[i] / kb / count[i] # [K]
    # end

    # # Find max speed in any one dimension
    # # adjust speed to handle collisions
    # maxSpeed = np.max(np.max(np.abs(self.particles.velocity)))
    # timeStepNew = atomRadius / maxSpeed
    # if timeStepNew < timeStepMin:
    #     timeStepMin = timeStepNew

    # # clear cumulative variables
    # measures.deltaMomentum = 0
    # measures.wallCollisions = 0
    # measures.gasCollisions = 0

    # profile.timeProperties += toc()

def finalize(params):
    # measures = params.measures
    # #. why avg over entire dataset? want steady state
    # averagePressure = np.mean(dataPressure) # [atm]
    # stdDevPressure = np.std(dataPressure)
    # averageTemperature = np.mean(dataTemperature) # [K]
    # averageCollisionRate = np.mean(dataGasCollisions) / nParticles * 1000 # [collisions/mlc/fs]

    # # Save final velocity
    # if includeVelocityHistogram:
    #     vxFinal = particles.velocity(:, 1)
    #     vFinal = sqrt(sum(particles.velocity .* particles.velocity, 2))
    pass

