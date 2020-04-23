"""
"""

import math
import numpy as np
from addict import Dict
from constants import *


def getNParticles(sim):
    # get total particles
    nparticles = 0
    for species in sim.species:
        nparticles += species.quantity
    return nparticles


def getPositions(distribution, quantity, ndimensions, innerBoxMatrix, radius):
    """get particle position distribution"""

    positions = None

    if distribution == 'random':
        # distribute particles randomly through container 
        # (keep away from walls by radius of atom)
        # self.position[iRange, :] = np.random.rand(quantity, self.ndimensions) * innerBoxMatrix + radius
        positions = np.random.rand(quantity, ndimensions) * innerBoxMatrix + radius

    # elif distribution == 'half':
    #     # species 1 in left side of box
    #     # species 2 in right side of box
    #     self.position[iRange, :] = np.random.rand(quantity, ndimensions) * innerBoxMatrix + radius
    #     self.position[iRange, 0] = self.position[iRange, 0] * 0.5 + boxSize[0]*iSpecies/2 # shift to left or right side of the box

    # elif distribution == 'test':
    #     # two particles symmetrically located in box
    #     self.position[0,:] = [1 * boxSize[0]/4, boxSize[1]/2, boxSize[2]/3]
    #     self.position[1,:] = [3 * boxSize[0]/4, boxSize[1]/2, boxSize[2]/3]

    # elif distribution == 'fcc':
    #     # arrange particles evenly throughout box volume
    #     # npod = n particles in one dimension
    #     for ix in range(npod):
    #         for iy in range(npod):
    #             for iz in range(npod):
    #                 n = iz + npod*(iy-1) + npod*npod*(ix-1)
    #                 self.position[n,1] = ix-1
    #                 self.position[n,2] = iy-1
    #                 self.position[n,3] = iz-1
    #     self.position = self.position / npod * box.matrix + boxSize[1]/npod/2

    # elif distribution == 'diff2':
    #     # simulate diffusion experiment:
    #     # species 1 - random
    #     # species 2 - circular distrib at center of box
    #     if iSpecies == 1:
    #         self.position[iRange, :] = np.random.rand(quantity, ndimensions) * innerBoxMatrix + radius
    #         self.position[iRange, 3] = np.ones(quantity) * boxSize[3]/2 # z's in middle
    #     else:
    #         theta = np.random.rand(quantity, 1) * 2 * math.pi
    #         rpos = np.random.rand(quantity, 1) * 3
    #         for j in range(quantity):
    #             n = j+iRange[1] - 1
    #             self.position[n, :] = [boxSize[1]/2 + rpos[j]*cos(theta[j]), boxSize[2]/2 + rpos[j]*sin(theta[j]), boxSize[3]/2]
    #         # self.position[iRange, :] = np.random.randn(quantity, ndimensions) * 5 + boxSize[1]/2
    #         self.position[iRange, 3] = np.ones(quantity) * boxSize[3]/2 # z's in middle
    
    # else:
    #     raise ValueError("Unknown distribution " + distribution)
    return positions


def getVelocities(distribution, quantity, ndimensions, vxRms, iRange):
    """get particle velocity distribution"""

    velocities = None

    if distribution == 'gaussian':
        # note: randn = normal (gaussian) distribution - multiply by std dev and add mean to get required distribution
        velocities = vxRms * np.random.randn(quantity, ndimensions)
        # now need to make sure the net energy is actually InitTemp - need to scale v distribution to get it to match.
        # otherwise the random numbers may give you a temperature different from what you expected.
        for dimension in range(0, ndimensions):
            actualRms = math.sqrt(np.mean(np.square(velocities[iRange, dimension]))) # eg 1.96 should be 2.03
            scale = vxRms / actualRms
            velocities[iRange, dimension] *= scale

    # elif distribution == 'flat':
    #     velocities = vxRms * (np.random.rand(quantity, ndimensions) - 0.5)

    # elif distribution == 'same':
    #     # all have same speed but random directions
    #     velocities = vxRms * np.sign(np.random.rand(quantity, ndimensions) - 0.5) 

    elif distribution == 'none':
        velocities = np.zeros((quantity, ndimensions))
    
    return velocities


def shiftParticles(position, radius):
    print('Shifting particles...')
    doneShifting = False
    while doneShifting == False:
        nShifts = 0
        doneShifting = True
        nParticles = len(position[:,0])
        print(nParticles)
        for i in range(0, nParticles - 1):
            for j in range(i + 1, nParticles):
                distanceVector = position[i, :] - position[j, :]
                distance = np.linalg.norm(distanceVector)
                if distance < (radius[i] + radius[j]):
                    position[i, :] = position[i, :] + radius[i]
                    position[j, :] = position[j, :] - radius[j]
                    nShifts = nShifts + 1
                    doneShifting = False
        print(f'    shifted {nShifts} particles')
    print('    done.')


# def getParticles(sim):
def initialize(sim):
    
    box = sim.box
    nparticles = getNParticles(sim)
    ndimensions = box.ndimensions
    sim.nparticles = nparticles # save for later
    sim.ndimensions = ndimensions

    # initialize arrays
    particles = Dict()
    particles.position = np.zeros((nparticles, ndimensions))
    particles.velocity = np.zeros((nparticles, ndimensions))
    particles.acceleration = np.zeros((nparticles, ndimensions))
    particles.mass = np.zeros(nparticles)
    particles.radius = np.zeros(nparticles)
    particles.color = [' '] * nparticles

    i = 0 # particle number
    for species in sim.species:
        # print(species)
        quantity = species.quantity # number of atoms of this species
        species.kT = kb * species.temperature # average thermal energy [Moules]
        vxRms = math.sqrt(species.kT / species.mass) # std deviation of one velocity component [A/ps]
        # atomVolume = 4/3 * math.pi * species.radius**3 # [A^3]
        innerBoxMatrix = box.matrix - 2 * species.radius * np.eye(3)
        iRange = slice(i, i + quantity) # range of indices for this species (eg 20:40)
        particles.mass[iRange] = species.mass
        particles.radius[iRange] = species.radius
        particles.color[iRange] = species.color
        particles.position[iRange, :] = getPositions(species.position, quantity, ndimensions, innerBoxMatrix, species.radius)
        particles.velocity[iRange, :] = getVelocities(species.velocity, quantity, ndimensions, vxRms, iRange)
        species.iRange = iRange # save for later
        i += quantity

    # make sure particles aren't colliding with each other...
    # if sim.shiftParticles:
    if sim.potentialType != 'none':
        shiftParticles(particles.position, particles.radius)
    
    # xRange = range(0, boxSize[0], nxSamples)

    # return particles
    sim.particles = particles


def update(sim):

    # get potential energy of particles
    particles = sim.particles
    potential = np.zeros(sim.nparticles)
    
    if sim.potentialType == 'Lennard-Jones':
        # Lennard-Jones 6-12 ideal gas potential
        # molecules appear neutral at large distances, become attractive closer, then repulsive close up
        #    U = 4 * epsilon * [ (sigma/r)^12 - (sigma/r)^6 ] (experimentally determined)
        #    F = - grad U = - 4 * epsilon * (-12 * (sigma^12)/(r^14) + 6 * (sigma^6)/(r^8)) * rvector 
        #                 = - 4 * epsilon * (-12 * (sigma/r)^12 + 6 * (sigma/r)^6 ) * rvector / r^2
        #    Argon: epsilon = 1.65e-21 J        sigma = 3.4 A
        #    Water: epsilon = 1.08e-21 J        sigma = 3.2 A
        epsilon = 99.6 # [Moules] well depth
        sigma = 3.4 # [Angstroms] internuclear distance where potential U is zero
        force = np.zeros((sim.nparticles, sim.ndimensions))
        for i in range(sim.nparticles - 1):
            for j in range(i + 1, sim.nparticles):
                distanceVector = particles.position[i,:] - particles.position[j,:]
                distance = np.linalg.norm(distanceVector)
                sigmaDistance = sigma / distance
                U = 4 * epsilon * (sigmaDistance**12 - 2 * sigmaDistance**6)
                Fij = - 4 * epsilon * (-12 * sigmaDistance**12 + 6 * sigmaDistance**6 ) * distanceVector / distance / distance
                force[i,:] += Fij
                force[j,:] -= Fij
                potential[i] += 0.5 * U
                potential[j] += 0.5 * U
            particles.acceleration[i,:] = force[i,:] / particles.mass[i]

    # save potential
    sim.particles.potential = potential
