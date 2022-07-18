# Lomb Periodogram

This is a python module that wraps a Fortran implementation of the 3-D Lomb periodogram.

## Documentation

The documentation of the python API can be found [here](https://pponsv.github.io/lomb_periodogram).
A description of the periodogram and a jupyter notebook with an example can also be found [here](./doc/)

## Features:

- Parallel (multi-core, not multi-cpu) Fortran implementation, wrapped to python using f2py (part of numpy).

- A simple plotting library is included.

- A synthetic signal generator is also included.

- Matlab code is included.

### Caveats:

- Developed and tested in a Linux environment. Build system only tested in Linux.

- Notes on the periodogram are incomplete.

## Requirements and compilation:

The Fortran code must be compiled and wrapped with f2py to be run.

### Requirements:

- gfortran compiler

- python3

- numpy

- matplotlib

- pdoc (to generate the documentation)

### Compilation:

In Linux, simply run `make` from the main directory.
