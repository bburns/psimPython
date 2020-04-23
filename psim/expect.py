"""
expect
Calculate expected values for experiment
"""

import numpy as np
from addict import Dict
from constants import *


def initialize(sim):

    expected = Dict()

    #. some of these are per species - how do? get avg over species or sum them?
    # expected.pressure = sim.nparticles * kT / sim.box.volume * atmospheresPerMascal # [atm]
    
    # get sum over species
    pressure = 0
    for species in sim.species:
        pressure += species.quantity * species.kT / sim.box.volume * atmospheresPerMascal # [atm]
        # print(species.quantity, species.kT, sim.box.volume, pressure)
    expected.pressure = pressure # ok?

    # expected.averageSpacing = (sim.box.volume / sim.nparticles) ** (1 / sim.ndimensions) # [A]
    # expected.speedRms = math.sqrt(3 * kT / atomMass) # [A/ps] #. init? per species yes?
    # expected.collisionRate = 4 * math.pi * math.sqrt(2) * atomRadius**2 * nparticles * expected.speedRms / box.volume * 1000 # [collisions/mlc/fs]
    # expected.meanFreeTime = 1 / expected.collisionRate # [ps]
    # expected.meanFreePath = expected.speedRms * expected.meanFreeTime # [A]
    # expected.mostProbableSpeed = math.sqrt(2 * kT / atomMass)
    # expected.averageSpeed = math.sqrt(8 * kT / math.pi / atomMass)
    # expected.volumeFraction = atomVolume * nparticles / box.volume
    # expected.massDensity = nparticles * atomMass / box.volume * kilogramsPerDalton / cubicMetersPerMolvo # [kg/m^3]

    # expected.pressure = 1
    expected.temperature = sim.species[0].temperature #. handle multiple species
    # expected.wallCollisions = 100 #...
    # expected.gasCollisions = 100 #...

    # # Maxwell-Boltzmann probability distribution
    # if includeVelocityHistogram
    #     speed = sqrt(kT / atomMass) # [A/ps]
    #     s = speed * (0:1/50:5) # speed range
    #     expectedSpeedDistribution = nparticles/2 * 4 * pi * (atomMass/(2*pi*kT))^(3/2) * (s.^2) .* exp(-0.5 * atomMass * s.^2 / kT) 
    #     s2 = speed * (-2:1/50:2) # 1 dim speed range
    #     expectedSpeedDistribution1d = nparticles/2 * sqrt (atomMass/(2*pi*kT)) * exp(-0.5 * atomMass * s2.^2 / kT)
    # end
    # if includeVelocityHistogram:
    #     speed = math.sqrt(kT / atomMass) # [A/ps]
    #     s = speed * np.linspace(0, 5, 250) # speed range
    #     sSquared = np.square(s) # ?
    #     expectedSpeedDistribution = nparticles/2 * 4 * math.pi * (atomMass/(2*math.pi*kT))^(3/2) * sSquared .* exp(-0.5 * atomMass * sSquared / kT) 
    #     s2 = speed * (-2:1/50:2) # 1 dim speed range
    #     expectedSpeedDistribution1d = nparticles/2 * sqrt (atomMass/(2*pi*kT)) * exp(-0.5 * atomMass * s2.^2 / kT)

    # return expected
    sim.expected = expected
