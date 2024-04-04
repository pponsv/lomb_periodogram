import numpy as np


def bandpass(sig: np.ndarray, flim: tuple, dt: float = 0.001):
    """
    Apply a simple bandpass filter to the input signal.

    Parameters:
        sig (array-like): The input signal.
        flim (tuple): The frequency limits (low, high) for the bandpass filter.
        dt (float, optional): The interval between samples (1/frequency). Default is 0.001.

    Returns:
        array-like: The filtered signal.
    """
    ff = np.fft.rfft(sig)
    fr = np.fft.rfftfreq(len(sig), dt)
    mask = (np.abs(fr) < flim[1]) & (np.abs(fr) > flim[0])
    ff -= ff * (~mask)
    nsig = np.fft.irfft(ff, len(sig))
    return nsig


def mat_bandpass(msig: np.ndarray, flim: tuple, dt: float = 0.001):
    """
    Simple bandpass filter for 2D arrays (along the second dimension)

    - Input:

        - `msig`: 2D array of signals, so that `msig[0]` is the first signal.

        - `flim`: Frequency limits (low, high)

        - `dt`: Interval between samples (1/frequency)
    """
    nmat = []
    for sig in msig:
        nmat.append(bandpass(sig, flim, dt))
    return np.array(nmat)


def detect_peaks(arr: np.ndarray, num: int = 3):
    """
    Simple peak-detecting algorithm for 2D arrays.

    *Must be improved*

    - Input:

        - `arr`: 2D array

        - `num`: Number of peaks we want to find

    - Outputs:

        - `peaks`: Array of peak indices
    """
    tmp = arr.copy()
    peaks = []
    for n in range(num):
        idx = np.unravel_index(np.argmax(tmp), tmp.shape)
        peaks.append(idx)
        for i in range(2):
            for j in range(3):
                try:
                    tmp[idx[0] - i, idx[1] - j] = 0
                    tmp[idx[0] - i, idx[1] + j] = 0
                    tmp[idx[0] + i, idx[0] + j] = 0
                    tmp[idx[0] + i, idx[0] - j] = 0
                except:
                    pass
    return np.array(peaks)
