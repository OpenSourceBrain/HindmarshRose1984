[![Continuous build using OMV](https://github.com/OpenSourceBrain/HindmarshRose1984/actions/workflows/omv-ci.yml/badge.svg)](https://github.com/OpenSourceBrain/HindmarshRose1984/actions/workflows/omv-ci.yml)

Hindmarsh Rose 1984 cell model
==============================

The Hindmarsh Rose model is a simplified point cell model which
captures complex firing patterns of single neurons, such as periodic
and chaotic bursting.

It has a fast spiking subsystem, which is a generalization of the
Fitzhugh-Nagumo system, coupled to a slower subsystem which allows the
model to fire bursts. 

The dynamical variables x,y,z correspond to the membrane potential, a
recovery variable, and a slower adaptation current, respectively.

# Simulation results

## For Regular Bursting

1) Membrane Potential (x)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/xreg.png)

2) Recovery Variable (y)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/yreg.png)

3) Slower Adaptation Current (z)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/zreg.png)


## For Chaotic Bursting

1) Membrane Potential (x)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/xch.png)

2) Recovery Variable (y)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/ych.png)

3) Slower Adaptation Current (z)

![alt text](https://github.com/doorkn-b/HindmarshRose1984/blob/master/Sim%20Images/zch.png)

Simulations conducted through [jNeuroML](https://github.com/NeuroML/jNeuroML).

Adding the environment variable JNML_HOME, pointing to the jNeuroML folder, as well as adding this path to the PATH variable will let you use the jnml utility from any folder.

or

```
./jnml LEMS_Regular_HindmarshRose.xml
./jnml LEMS_Chaotic_HindmarshRose.xml
```
from within the file.

Simulated by https://github.com/doorkn-b



This model firstly appeared in:
Hindmarsh J. L., and Rose R. M. (1984) A model of neuronal bursting
using three coupled first order differential equations.  Proc. R. Soc.
London, Ser. B 221:87–102.




