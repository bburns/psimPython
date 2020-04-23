"""
Integrate particle positions and handle wall and particle collisions
"""

import numpy as np


def update(params):
    measures = params.measures
    particles = params.particles

    if params.potentialType == 'none': # no acceleration
        particles.position += (params.timedelta * particles.velocity)

    elif params.potentialType == 'Lennard-Jones':
        # # Verlet Algorithm
        # # we always need the last two values of position to produce the next one...
        # # [Thijssen p475]
        # # x(t+h) = 2x(t) - x(t-h) + h^2*a(x(t))
        # # tic()
        # positionNew = None
        # if params.ntimestep == 0:
        #     # for first step, don't have previous position yet
        #     positionNew = particles.position + (params.timedelta * particles.velocity) + (0.5 * params.timedelta ** 2 * particles.acceleration)
        #     particles.velocity = particles.velocity + params.timedelta * particles.acceleration
        # else:
        #     positionNew = 2 * particles.position - params.positionOld + params.timedelta ** 2 * particles.acceleration
        #     particles.velocity = (positionNew - params.positionOld) / 2 / params.timedelta
        # params.positionOld = particles.position
        # particles.position = positionNew
        # # profile.timeIntegrate += toc()
        if params.ntimestep == 0:
            particles.position += particles.velocity * params.timedelta
            # particles.velocity += particles.acceleration * params.timedelta
            params.oldAcceleration = particles.acceleration
        else:
            particles.position += particles.velocity * params.timedelta + 0.5 * particles.acceleration * params.timedelta**2
            particles.velocity += 0.5 * (params.oldAcceleration + particles.acceleration) * params.timedelta
            params.oldAcceleration = particles.acceleration
    else:
        raise ValueError("Unknown potentialType " + params.potentialType)


    #-----------------------------------------------------------------------------------
    # Handle Wall Collisions
    #-----------------------------------------------------------------------------------
    # Check for collision with walls
    # Flip momentum component normal to wall
    # These are cumulative variables, cleared after each sample taken. 
    # tic()
    for i in range(params.nparticles):
        for j in range(params.ndimensions):
            if particles.position[i, j] < particles.radius[i]:
                particles.velocity[i, j] = -particles.velocity[i, j]
                particles.position[i, j] = 2 * particles.radius[i] - particles.position[i, j] # reflect about x=r axis
                measures.deltaMomentum += abs(2*particles.mass[i]*particles.velocity[i, j]) # [DA/ps]
                measures.wallCollisions += 1
            elif particles.position[i, j] > (params.boxsize[j] - particles.radius[i]):
                particles.velocity[i, j] = -particles.velocity[i, j]
                particles.position[i, j] = 2 * (params.boxsize[j] - particles.radius[i]) - particles.position[i, j] # reflect about x=L-r axis
                measures.deltaMomentum += abs(2*particles.mass[i]*particles.velocity[i, j]) # [DA/ps]
                measures.wallCollisions += 1
    # profile.timeWalls += toc()

    # # Check for collision with semi-permeable membrane
    # # species 0 can cross, species 1 can't
    # if includeMembrane:
    #     for i in species(1).jRange:
    #         if particles.position[i,0] < (MembranePosition + particles.radius[i]):
    #             particles.velocity[i,0] = -particles.velocity[i,0]
    #             particles.position[i,j] = 2 * (MembranePosition + particles.radius[i]) - particles.position[i,j] # reflect about x=m+r axis


    #-----------------------------------------------------------------------------------
    # Handle Gas Collisions
    #-----------------------------------------------------------------------------------
    # Check for collision with other particles
    # This is the slowest part of the program. 
    # Swap momentum components parallel to vector connecting particles
    #. need smarter collision detector - ie trace each back to point where just touching to find correct distance vector
    # tic()
    if params.includeGasCollisions:
        for i in range(params.nparticles - 1):
            for j in range(i + 1, params.nparticles):
                distanceVector = particles.position[i,:] - particles.position[j,:]
                distance = np.linalg.norm(distanceVector) 
                if distance < (particles.radius[i] + particles.radius[j]):
                    velocityVector = particles.velocity[i,:] - particles.velocity[j,:]
                    distanceHat = distanceVector / distance
                    velocityComponent = np.dot(distanceHat, velocityVector) * distanceHat
                    particles.velocity[i,:] = particles.velocity[i,:] - velocityComponent
                    particles.velocity[j,:] = particles.velocity[j,:] + velocityComponent
                    measures.gasCollisions += 1
    # profile.timeGas += toc()
