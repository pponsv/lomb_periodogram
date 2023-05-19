from . import flomb as fl
from .main import *
from .synth import *
from .plots import *


def easylomb3(*args, **kwargs):
    r"""
    Calculates the lomb periodogram for an array of signals at different positions
    (given by their magnetic coordinates).

    $$
        P(\omega, n, m) = \dfrac{1}{YY}
        \left(
            \dfrac{\left[\sum_i y_i \cos(\alpha_i - \tau)\right]^2}{\sum_i \cos^2 (\alpha_i - \tau)}
            +
            \dfrac{\left[\sum_i y_i \sin(\alpha_i - \tau)\right]^2}{\sum_i \sin^2 (\alpha_i - \tau)}
        \right)
    $$

    where:

    - $\alpha$ is given by:

    $$
        \tan 2 \tau = \dfrac{\sum_i \sin 2\alpha_i}{\sum_i \cos 2\alpha_i}
    $$

    - $YY$ is given by:

    $$
        \text{YY} = \sum_i y_i^2
    $$

    Wrapper around the fortran code.

    - Input:

        -`time` : time array. Input rank-1 array('d') with bounds (ntime)

        -`thetas` : poloidal angles. Input rank-1 array('d') with bounds (ncoils)

        -`phis` : toroidal angles. Input rank-1 array('d') with bounds (ncoils)

        -`sigs` : signal matrix. Input rank-2 array('d') with bounds (ncoils,ntime)

        -`f` : frequency at which the analysis is performed. Input float

        -`ns` : toroidal mode numbers at which the analysis is performed. Input rank-1 array('d') with bounds (nn)

        -`ms` : poloidal mode numbers at which the analysis is performed. Input rank-1 array('d') with bounds (nm)

    - Output:

        -`mapa`: 2D-array with the values of the periodogram
    """
    return fl.easylomb3(*args, **kwargs).T


def easylomb2(*args, **kwargs):
    r"""
    Same as above, but considering one angle equal to zero.


    Wrapper around the fortran code.

    - Input:

        -`time` : time array. Input rank-1 array('d') with bounds (ntime)

        -`thetas` : poloidal angles. Input rank-1 array('d') with bounds (ncoils)

        -`sigs` : signal matrix. Input rank-2 array('d') with bounds (ncoils,ntime)

        -`f` : frequency at which the analysis is performed. Input float

        -`ms` : poloidal mode numbers at which the analysis is performed. Input rank-1 array('d') with bounds (nm)

    - Output:

        -`mapa`: 1D-array with the values of the periodogram
    """
    return fl.easylomb2(*args, **kwargs)


# ~ __all__ = ["plot"]
