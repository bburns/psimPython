#-----------------------------------------------------------------------------------
# Constants and Units
#-----------------------------------------------------------------------------------
# mass:       Daltons (D) (1.66e-26 kg)
# Length:     Angstroms (A) (1e-10 m)
# Time:       Picosecs (ps) (1e-12 sec)
#
# force:      mewton "Molecular Newton" = DA/ps^2 
# Energy:     moule "Molecular Joule" = DA^2/ps^2 
# pressure:   mascal "Molecular Pascal" = D/A/ps^2 
# volume:     molvo "Molecular volume" = A^3 
#-----------------------------------------------------------------------------------

avogadro = 6.022e23 # Avogadro's number
kbJoules = 1.380658e-23 # Boltzmann's constant [Joules/K]
dalton = 1.6605402e-27 # [kg]
angstrom = 1e-10 # [meters]
ps = 1e-12 # [seconds]
kjpermol = 1000 / avogadro # [1.66e-21 J]
eV = 1.602e-19 # [Joules]

# define custom molecular units (see above)
mewton = dalton * angstrom / ps**2 # [Newtons]
moule = dalton * angstrom**2 / ps**2 # [Joules]
mascal = mewton / angstrom**2 # [Pascals]
molvo = angstrom**3 # [m^3]

# Conversion Factors
newtonsPerMewton = mewton # [1.66054e-13 Newtons/mewton]
joulesPerMoule = moule # [1.66054e-23 Joules/moule]
pascalsPerMascal = mascal # [1.66054e7 Pascal/mascal]
mewtonsPerNewton = 1/mewton # [6.022137377e12 Mewtons/Newton]
moulesPerJoule = 1/moule # [6.022137e22 Moules/Joule]
mascalsPerPascal = 1/mascal # [6.022137e-8 mascal/Pascal]
angstromsPerMeter = 1/angstrom
kilogramsPerDalton = dalton
cubicMetersPerMolvo = angstrom**3
eVperMoule = moule / eV # [eV/moule]
eVperJoule = 1/eV # [eV/Joule]
atmospheresPerPascal = 1/101325 # [Atm/Pa]
atmospheresPerMascal = atmospheresPerPascal * pascalsPerMascal # [Atm/mascal]

kb = kbJoules * moulesPerJoule # Boltzmann's constant [0.83145116 Moules/K]
g = 9.8 * angstromsPerMeter / (1e12)**2 # acceleration of gravity [9.8e-14 A/ps^2]
speedOfLight = 3e8 * 1e10/1e12 # [3e6 A/ps]

