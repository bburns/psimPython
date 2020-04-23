"""
psim
Python Particle Simulator
"""

from params import params # the experiment params
import experiment


experiment.initialize(params)
experiment.run()
experiment.finalize()
