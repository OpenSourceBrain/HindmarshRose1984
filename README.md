[![Continuous build using OMV](https://github.com/OpenSourceBrain/HindmarshRose1984/actions/workflows/omv-ci.yml/badge.svg)](https://github.com/OpenSourceBrain/HindmarshRose1984/actions/workflows/omv-ci.yml)

HindmarshRose1984
=================

HindmarshRose 1984 cell model

The Hindmarsh Rose model is a simplified point cell model which
captures complex firing patterns of single neurons, such as periodic
and chaotic bursting.

It in a fast spiking subsystem, which is a generalization of the
Fitzhugh-Nagumo system, coupled to a slower subsystem which allows the
model to fire bursts. 

The dynamical variables x,y,z correspond to the membrane potential, a
recovery variable, and a slower adaptation current, respectively.

This model firstly appeared in:
Hindmarsh J. L., and Rose R. M. (1984) A model of neuronal bursting
using three coupled first order differential equations.  Proc. R. Soc.
London, Ser. B 221:87–102.
