# psim (Particle Simulator)

psim is a particle simulator that puts a number of particles in a box, measures various thermodynamic properties, and compares them with expected values. 


## Goals

### Physics

- run small-scale thermodynamic experiments for entropy, enthalpy, reaction kinetics
- use dimensionless parameters - output with real units
 
### Programming

- structure a Python project by breaking it down into smaller modules
- define tests to make sure program math is working as expected
- set up continuous integration to run tests while developing - use Travis CI and GitHub (?)
- track code coverage of tests and aim for 100%
- use venv or conda environment (or Docker?)
- use squashed commits for cleaner repo history
- make sure runs cross-platform on Windows, Mac, Linux
- maintain minimal contact between modules [currently passing things through namespaces - better way? define fns?]
- make realtime charts and visualizations
- export trajectory data and display in other programs
- try pypy for speed
- reimplement in Julia and compare speed
- reimplement in JavaScript with visualizations and compare speed

### Reporting

- write a report summarizing findings
- explain how to hack on the app and write more experiments


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
    python psim


## Developing

The source is in `psim` - running `python psim` will load the file `psim/__main__.py` (a Python convention).


## Testing

Tests are run with **pytest-watch**, which runs **pytest** when source files change - 

    pytest-watch

or

    ptw


## Configuration

Configuration files

- .travis[-off].yml - Travis continuous integration settings - when on, builds and tests the app on different OS's and configurations. Build status and history is available at https://travis-ci.org/github/bburns/psimPython
- environment.yml - list of dependencies, as used by the conda package manager
- requirements.txt - list of dependencies, as used by the pip Python package manager
- .env - environment variables
- .gitignore - files for git to ignore


## License

MIT
