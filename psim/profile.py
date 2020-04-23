from addict import Dict

def initialize(params):
    profile = Dict()
    # Initialize profile values
    profile.timeWalls = 0
    profile.timeGas = 0
    profile.timeProperties = 0
    profile.timeDisplay = 0
    profile.timeIntegrate = 0
    # return profile
    params.profile = profile
    
