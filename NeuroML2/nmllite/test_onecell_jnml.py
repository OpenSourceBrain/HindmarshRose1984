import os, sys

from neuromllite.utils import load_simulation
from neuromllite.NetworkGenerator import generate_and_run

sim = load_simulation('SimOneCell.json')

generate_and_run(sim, simulator="jNeuroML")