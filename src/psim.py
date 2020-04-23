"""psim.py - Python Particle Simulation

psim simulates a number of particles confined to box, calculates various
thermodynamic properties, and compares them with expected values.
"""

from params import params # the experiment params
import experiment


experiment.initialize(params)
experiment.run()
experiment.finalize()
