"""
params
read in experiment parameters from file specified at console, or a default file.
"""

import sys
import hjson # "human json" - an easy to read format for config files


# access dict keys as attributes - eg can say foo.bar instead of foo['bar']
# see https://stackoverflow.com/a/59379520/243392
from addict import Dict


# default experiment to use if none specified
defaultfile = './experiments/idealGasLaw.hjson'

# get filename from console
paramfile = sys.argv[1] if len(sys.argv)>1 else defaultfile

# read the file to a string (hjson format)
s = open(paramfile, 'r').read()

# parse the hjson into an ordered dictionary
orderedDict = hjson.loads(s)

# convert the dictionary into an addict Dict
params = Dict(orderedDict)


if __name__ == '__main__':
    print(params.meta.name)
    print(params)
