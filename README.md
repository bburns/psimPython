# psim (Particle Simulator)

psim is a particle simulator that puts a number of particles in a box, measures various thermodynamic properties, and compares them with expected values. 


## Goals

### Physics

- run small-scale thermodynamic experiments for entropy, enthalpy, reaction kinetics
- use dimensionless parameters - output with real units
 
### Programming

- try structuring a Python project by breaking it down into smaller files
- maintain minimal contact between modules [currently passing things through namespaces - better way? define fns?]
- make realtime charts and visualizations
- export trajectory data and display in other programs
- try pypy for speed?
- reimplement in Julia and compare speed
- reimplement in JavaScript with visualizations


## Experiments

psim can run different experiments - see the `experiments` folder - 

- Ideal Gas Law (PV=nRT)
- Maxwell Velocity Distribution
- Heat Flow
- Diffusion
- Gas with Lennard-Jones potential

Future experiments could include -

- Brownian Motion
- Osmosis
- Membrane Potential
- Speed of Sound
- Heat Capacities
- Enthalpy
- Entropy
- Free Energy
- Water
- Liquid-Gas Equilibrium
- Joule-Thompson Effect


## Setup

    git clone psimPython


## Running

    cd psimPython
    python src/psim.py


## License

MIT
