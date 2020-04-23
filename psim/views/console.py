import datetime


def printData(name, value, units=""):
    print(f"""{name:<30}{value} {units}""")


def initialize(sim):

    print(f"""
------------------------------------------------------------------------------------------
psim
Particle Simulator
Current time: {datetime.datetime.now()}
------------------------------------------------------------------------------------------
Experiment: {sim.name}
{sim.description}
""")
    printData("Box Size:", f"{sim.boxsize[0]}x{sim.boxsize[1]}x{sim.boxsize[2]} A")
    printData("Volume:", f"{sim.box.volume} A^3")
    printData("Number of Particles:", sim.nparticles)
    printData("Time Range:", f"{sim.duration} ps")
    printData("Time Step:", f"{sim.timedelta} ps")
    printData("Include Gas Collisions:", f"{sim.includeGasCollisions or 'no'}")
    printData("Potential Type:", sim.potentialType)
    print()

    for species in sim.species:
        printData("Species:", species.name)
        printData("Mass:", f"{species.mass:.1f} D")
        printData("Radius:", f"{species.radius:.1f} A")
        printData("Init Temperature:", f"{species.temperature} K")
        printData("Init Particle Distribution:", species.position)
        printData("Init Velocity Distribution:", species.velocity)
        # printData("Init Rms Speed:", f"{self.expectedSpeedRms:.1f} A/ps")
        # printData("Avg Intermolecular Spacing:            {self.expectedAverageSpacing:.2f} A")
        # printData("VolumeFraction: {self.volumeFraction:.2f} (particle volume / total volume)")
        # printData("MassDensity: {self.massDensity:.2f} kg/m^3")
        print()


def update(sim):
    print("Time:", sim.currentTime, sim.measures.pressure)
    # print(sim.particles.position[0,0])

def finalize(sim):
    samples = sim.samples
    print(f"""
Results
Pressure: {samples.pressure}
""")
#                         Expected              Measured (avg)   StdDev                
# Pressure:              {expected.pressure:9.2f}              {averagePressure:9.2f}      {stdDevPressure:9.2f}  atm
# Temperature:           {initTemperature:9.1f}              {averageTemperature:9.1f}  K
# CollisionRate:         {expectedCollisionRate:9.2f}              {averageCollisionRate:9.2f}  collisions/mlc/fs

# Time Requirements:
#         Wall Collisions:       {timeWalls:.1f} sec
#         Gas Collisions:        {timeGas:.1f} sec
#         Calculate Properties:  {timeProperties:.1f} sec
#         Display Data:          {timeDisplay:.1f} sec
#         Integrate:             {timeIntegrate:.1f} sec
# """)
#             if timeStepMin < timeDelta:
#                 print(f"Need to reduce time step! currently {timeDelta:.3f} ps, should be {timeStepMin:.3f} ps")


if __name__ == '__main__':
    from addict import Dict
    initialize(Dict())
