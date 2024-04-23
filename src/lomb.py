from ..bin.flomb import lomb_f

r"""
The Lomb periodogram for an array of signals at different positions (given by their magnetic 
coordinates) is given by:
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
    $$  \tan 2 \tau = \dfrac{\sum_i \sin 2\alpha_i}{\sum_i \cos 2\alpha_i}  $$
- $YY$ is given by:
    $$  \text{YY} = \sum_i y_i^2    $$
"""


def easylomb3_difftimes(time, thetas, phis, sigs, f, ns, ms):
    """
    Calculate the lomb periodogram for an array of signals at different positions.
    The signals are given as a vector

    Parameters:
    time (array-like): The time values of the data points.
    thetas (array-like): The theta values of the data points.
    phis (array-like): The phi values of the data points.
    sigs (array-like): The signal array.
    f (float): The frequency at which to calculate the periodogram.
    ns (int): The array of toroidal mode numbers in which to calculate the periodogram.
    ms (int): The array of poloidal mode numbers in which to calculate the periodogram.

    Returns:
    array-like: The lomb periodogram values.

    """
    return lomb_f.easylomb3_difftimes(time, thetas, phis, sigs, f, ns, ms).T


def easylomb3(time, thetas, phis, sigs, f, ns, ms):
    r"""
    Calculates the lomb periodogram for an array of signals at different positions.
    The signals are given as a matrix
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
    return lomb_f.easylomb3(time, thetas, phis, sigs, f, ns, ms).T


def easylomb2(time, thetas, sigs, f, ms):
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
    return lomb_f.easylomb2(time, thetas, sigs, f, ms)
