import h5py
import numpy as np
import matplotlib as mpl
import matplotlib.axes as mpl_axes
import matplotlib.pyplot as plt

from .lomb import easylomb2, easylomb3, easylomb3_difftimes
from .plots import plotmapa_alone_ax


def read_dataset(f: h5py.File, name: str, kind: str):
    dat = f[name]
    assert isinstance(dat, h5py.Dataset)
    if kind == "vec":
        return dat[:]
    elif kind == "num":
        return dat[()]


class Lomb_vec:
    ax: mpl_axes.Axes

    def __init__(
        self,
        time: np.ndarray,
        thetas: np.ndarray,
        phis: np.ndarray,
        sigs: np.ndarray,
        nmax: int = 15,
        mmax: int = 15,
    ):
        self.time = time
        self.thetas = thetas
        self.phis = phis
        self.sigs = sigs
        self.ns = np.arange(-nmax, nmax + 1)
        self.ms = np.arange(-mmax, mmax + 1)

    def easylomb3_difftimes(self, f0: float):
        self.f0 = f0
        self.mapa = easylomb3_difftimes(
            self.time,
            self.thetas,
            self.phis,
            self.sigs,
            self.f0,
            self.ns,
            self.ms,
        )

    def plotmapa(self, ax: mpl_axes.Axes | None = None):
        assert hasattr(
            self, "mapa"
        ), "You must calculate the periodogram first"
        if ax is None:
            fig = plt.figure(figsize=(3.39, 3.39))
            ax = fig.add_subplot(1, 1, 1)
        self.ax = ax
        self.fig = ax.get_figure()
        plotmapa_alone_ax(self.mapa, self.ns, self.ms, ax=self.ax)
        return self.ax.get_figure(), self.ax

    def to_hdf(self, filename: str):
        with h5py.File(filename, "w") as f:
            f.create_dataset("time", data=self.time)
            f.create_dataset("thetas", data=self.thetas)
            f.create_dataset("phis", data=self.phis)
            f.create_dataset("sigs", data=self.sigs)
            f.create_dataset("ns", data=self.ns)
            f.create_dataset("ms", data=self.ms)
            f.create_dataset("mapa", data=self.mapa)
            f.create_dataset("f0", data=self.f0)

    @classmethod
    def read_hdf(cls, filename: str):
        inst = cls.__new__(cls)
        with h5py.File(filename, "r") as f:
            inst.time = read_dataset(f, "time", "vec")
            inst.thetas = read_dataset(f, "thetas", "vec")
            inst.phis = read_dataset(f, "phis", "vec")
            inst.sigs = read_dataset(f, "sigs", "vec")
            inst.ns = read_dataset(f, "ns", "vec")
            inst.ms = read_dataset(f, "ms", "vec")
            inst.mapa = read_dataset(f, "mapa", "vec")
            inst.f0 = read_dataset(f, "f0", "num")
        return inst
