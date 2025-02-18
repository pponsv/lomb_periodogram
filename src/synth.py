import numpy as np
from dataclasses import dataclass


@dataclass
class Mode:
    m: int
    n: int
    f: float
    amp: complex

    def __call__(self):
        return np.array([self.m, self.n, self.f, self.amp])


@dataclass
class Modes:
    modes: list[Mode]

    def __iter__(self):
        return iter(self.modes)

    def __getitem__(self, index):
        return self.modes[index]

    def __add__(self, other):
        if isinstance(other, Mode):
            return Modes(self.modes + [other])
        elif isinstance(other, Modes):
            return Modes(self.modes + other.modes)

    def __call__(self):
        return np.array([mode() for mode in self.modes])

    @classmethod
    def from_array(cls, array):
        return cls([Mode(*mode) for mode in array])


def single_signal_noise(t, modes, theta, phi, anoise=0.2, pnoise=0.2):
    """
    Makes a signal, optionally with amplitude and/or phase noise.

    - Inputs:

        - `t`
    """
    if not isinstance(modes, Modes):
        modes = Modes.from_array(modes)
    fac = np.sum(np.abs([mode.amp for mode in modes])) * anoise
    sig = np.zeros(t.shape, dtype=np.complex128)
    for mode in modes:
        # m, n, f, amp = mode()
        tmpnoise = 2 * np.pi * pnoise * np.random.normal(0, pnoise, t.shape)
        sig += mode.amp * np.exp(
            1j
            * (
                mode.m * theta
                + mode.n * phi
                - 2 * np.pi * mode.f * t
                + tmpnoise
            )
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
