# Lomb Periodogram

This is a python module that wraps a Fortran implementation of the 3-D Lomb periodogram.

## Features:

- Parallel (multi-core, not multi-cpu) Fortran implementation, wrapped to python using f2py (part of numpy).

- A simple plotting library is included.

- A synthetic signal generator is also included.

### Caveats:

- Developed and tested in a Linux environment. Build system only tested in Linux.

## Requirements and compilation:

The Fortran code must be compiled and wrapped with f2py to be run.

### Requirements:

- gfortran compiler

- python3

- numpy

- matplotlib

### Compilation:

In Linux, simply run `make` from the main directory.
