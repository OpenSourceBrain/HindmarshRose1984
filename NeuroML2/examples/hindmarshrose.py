#!/usr/bin/env python3
"""
Simulating a regular spiking HR neuron with NeuroML.

File: hindmarshrose.py
"""

from neuroml import NeuroMLDocument
import neuroml.writers as writers
from neuroml.utils import component_factory, validate_neuroml2
from pyneuroml import pynml
from pyneuroml.plot import generate_plot
from pyneuroml.lems import LEMSSimulation
import numpy as np

nml_doc = component_factory("NeuroMLDocument", id="HindmarshRoseNeuron")
hr0 = nml_doc.add("HindmarshRose1984Cell", id="hr_regular", a="1.0", b="3.0", c="-3.0", d="5.0", s="4.0", x1="-1.3", r="0.002", x0="-1.1", y0="-9", z0="1.0", C="28.57142857pF", v_scaling="35.0mV")
net = nml_doc.add("Network", id="HRNet", validate=False)
# Create a population of defined cells and add it to the model
pop0 = net.add("Population", id="HRPop0", component=hr0.id, size=1)

# add external stimulus it to the model
pg = nml_doc.add("PulseGenerator", id="pulseGen_%i" % 0, delay="0s", duration="1000s", amplitude="5nA")
exp_input = net.add("ExplicitInput", target="%s[%i]" % (pop0.id, 0), input=pg.id, destination="synapses")

# Write the NeuroML model to a file
nml_file = 'hindmarshrose1984_single_cell_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)

# Validate the NeuroML model against the NeuroML schema
validate_neuroml2(nml_file)

# Create a simulation instance of the model
simulation_id = "example-single-hindmarshrose1984cell-sim"
simulation = LEMSSimulation(sim_id=simulation_id, duration=1.4e3, dt=0.0025, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

# Define the output file and record membrane potential
simulation.create_output_file("output0", "%s.v.dat" % simulation_id)
simulation.add_column_to_output_file("output0", 'HRPop0[0]', 'HRPop0[0]/v')

# Save and run the simulation using the jNeuroML simulator
lems_simulation_file = simulation.save_to_file()
pynml.run_lems_with_jneuroml(lems_simulation_file, max_memory="2G", nogui=True, plot=False)

# load data and plot
data_array = np.loadtxt("%s.v.dat" % simulation_id)
generate_plot([data_array[:, 0]], [data_array[:, 1]], "Membrane potential", show_plot_already=True, save_figure_to="%s-v.png" % simulation_id, xaxis="time (s)", yaxis="membrane potential (V)", font_size=16, bottom_left_spines_only=True)
