"""
box
Defines the box and compartments, if any. 
"""

from addict import Dict
import numpy as np

#. handle 2d, 3d

def initialize(params):
    boxsize = params.boxsize
    box = Dict()
    box.ndimensions = len(boxsize)
    box.matrix = np.matrix([[boxsize[0], 0, 0], [0, boxsize[1], 0], [0, 0, boxsize[2]]])
    box.area = 2 * (boxsize[0] * boxsize[1] + boxsize[1] * boxsize[2] + boxsize[0] * boxsize[2]) # [A^2] ie 2LH + 2HW + 2LW
    box.volume = boxsize[0] * boxsize[1] * boxsize[2] # [A^3]
    params.box = box
