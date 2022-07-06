import numpy as np

def single_signal_noise(t, modes, theta, phi, anoise=0.2, pnoise=0.2):
    modes = np.array(modes)
    assert modes.shape[1]==4, 'Modes not shaped well'
    fac = np.sum(np.abs(modes[:,3]))*anoise
    sig = np.zeros(t.shape, dtype=np.complex128)
    for mode in modes:
        m, n, w, amp  = mode
        tmpnoise      = 2*np.pi*pnoise*np.random.normal(0,pnoise,t.shape)
        sig          += amp*np.exp(1j*(-w*t + m*theta + n*phi + tmpnoise))
    return np.real(sig + (np.random.rand(len(t))-0.5)*fac)


def csignal(t, modes, thetas, phis, anoise=0.2, pnoise=0.2):
    smatrix = []
    for theta, phi in zip(thetas, phis):
        smatrix.append(single_signal_noise(t, modes, theta=theta, phi=phi, anoise=anoise, pnoise=pnoise))
    return np.array(smatrix)
