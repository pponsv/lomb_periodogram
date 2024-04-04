import numpy as np


def single_signal_noise(t, modes, theta, phi, anoise=0.2, pnoise=0.2):
    """
    Makes a signal, optionally with amplitude and/or phase noise.

    - Inputs:

        - `t`
    """
    modes = np.array(modes)
    assert modes.shape[1] == 4, "Modes not shaped well"
    fac = np.sum(np.abs(modes[:, 3])) * anoise
    sig = np.zeros(t.shape, dtype=np.complex128)
    for mode in modes:
        m, n, f, amp = mode
        tmpnoise = 2 * np.pi * pnoise * np.random.normal(0, pnoise, t.shape)
        sig += amp * np.exp(
            1j * (m * theta + n * phi - 2 * np.pi * f * t + tmpnoise)
        )
    return np.real(sig + (np.random.rand(len(t)) - 0.5) * fac)


def csignal(t, modes, thetas, phis, anoise=0.2, pnoise=0.2):
    """
    Makes a matrix of signals, optionally with amplitude and/or phase noise

    modes: [[m, n, f, amp], ...]
    """
    smatrix = []
    for theta, phi in zip(thetas, phis):
        smatrix.append(
            single_signal_noise(
                t, modes, theta=theta, phi=phi, anoise=anoise, pnoise=pnoise
            )
        )
    return np.array(smatrix)
