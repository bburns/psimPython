"""
views
includes console output, charts, and 2d/3d visualizations. 
"""

# for some reason can't just say `import charts` etc here
from . import charts
from . import console
from . import visualizations


def initialize(sim):
    console.initialize(sim)
    if sim.showCharts: charts.initialize(sim)
    if sim.show3d: visualizations.initialize(sim)

def update(sim):
    console.update(sim)
    if sim.showCharts: charts.update(sim)
    if sim.show3d: visualizations.update(sim)

def finalize(sim):
    console.finalize(sim)
    if sim.showCharts: charts.finalize(sim)
    if sim.show3d: visualizations.finalize(sim)
