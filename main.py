import numpy as np


def bandpass(sig, flim, dt=0.001):
    """
    Simple bandpass filter.

    - Input:

        - `sig`: 1D array, signal.

        - `flim`: Frequency limits (low, high)

        - `dt`: Interval between samples (1/frequency)
    """
    ff = np.fft.rfft(sig)
    fr = np.fft.rfftfreq(len(sig), 0.001)
    mask = (np.abs(fr)<flim[1]) & (np.abs(fr)>flim[0])
    ff -= ff*(~mask)
    nsig = np.fft.irfft(ff, len(sig))
    return nsig

def mat_bandpass(msig, flim, dt=0.001):
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

def detect_peaks(arr, num=3):
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
                    tmp[idx[0]-i, idx[1]-j] = 0
                    tmp[idx[0]-i, idx[1]+j] = 0
                    tmp[idx[0]+i, idx[0]+j] = 0
                    tmp[idx[0]+i, idx[0]-j] = 0
                except:
                    pass
    return np.array(peaks)







if __name__ == "__main__":
    pass
