from neuromllite import Network, Cell, InputSource, Population, Synapse
from neuromllite import Projection, RandomConnectivity, Input, Simulation
import sys
from neuromllite.NetworkGenerator import check_to_generate_or_run


def generate(ref):

    ################################################################################
    ###   Build new network

    net = Network(id=ref)
    net.notes = "Example: HindmarshRose"
    net.parameters = {"N": 1}

    cell = Cell(id="hr_regular0", lems_source_file="../HindmarshRose3d.xml")
    cell.parameters = {}

    params = {
        "a": 1,
        "b": 3,
        "c": -3.0,
        "d": 5.0,
        "s": 4.0,
        "I": 5.0,
        "x1": -1.3,
        "r": 0.002,
        "x0": -1.1,
        "y0": -9,
        "z0": 1.0,
    }

    for p in params:
        cell.parameters[p] = p
        net.parameters[p] = params[p]

    net.cells.append(cell)


    pop = Population(
        id="hrPop", size="1", component=cell.id, properties={"color": ".7 0 0"}
    )
    net.populations.append(pop)


    print(net)
    print(net.to_json())
    new_file = net.to_json_file("%s.json" % net.id)


    ################################################################################
    ###   Build Simulation object & save as JSON

    sim = Simulation(
        id="Sim%s"%net.id,
        network=new_file,
        duration="1400000",
        dt="2.5",
        record_variables={"x": {"all": "*"}, "y": {"all": "*"}, "z": {"all": "*"}},
        plots2D={
            "X-Y": {"x_axis": "hrPop[0]/x", "y_axis": "hrPop[0]/y"},
            "Y-Z": {"x_axis": "hrPop[0]/y", "y_axis": "hrPop[0]/z"},
            "X-Z": {"x_axis": "hrPop[0]/x", "y_axis": "hrPop[0]/z"},
        },
        plots3D={
            "X-Y-Z": {
                "x_axis": "hrPop[0]/x",
                "y_axis": "hrPop[0]/y",
                "z_axis": "hrPop[0]/z",
            }
        },
    )

    sim.to_json_file()

    return sim, net



if __name__ == "__main__":

    sim, net = generate(ref="OneCell")

    ################################################################################
    ###   Run in some simulators

    import sys

    check_to_generate_or_run(sys.argv, sim)