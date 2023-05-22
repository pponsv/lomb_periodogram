import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
from matplotlib.ticker import MultipleLocator
from .main import detect_peaks


def plotlomb2(x, y, xlabel="m", title=""):
    """
    Plots the 2D lomb periodogram.
    """
    fig, ax = plt.subplots(1, 1, figsize=[5, 3])
    ax.bar(x, y)
    ax.set(ylabel="P [a.u]", xlabel="m", title=title)
    return fig, ax


def plotmapa(mapa, ns, ms, norm=None, npeaks=3, title="", fig=None):
    """
    Plots the 3D lomb periodogram, and optionally finds the points with maxima.
    """
    peaks = detect_peaks(mapa, npeaks)
    # mapa=mapa.T
    if fig is None:
        fig = plt.figure(
            figsize=[9, 6], constrained_layout=False, tight_layout=False, dpi=100
        )
    gs = gridspec.GridSpec(
        2,
        4,
        wspace=0.1,
        hspace=0.1,
        width_ratios=[8, 2, 0.5, 0.3],
        height_ratios=[4, 1],
    )
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    ax3 = fig.add_subplot(gs[0, 1], sharey=ax1)
    axcm = fig.add_subplot(gs[0, 3])
    axtitle = fig.add_subplot(gs[1, 1:])
    axtitle.set_axis_off()
    axtitle.text(
        0.5,
        0.3,
        title,
        fontsize=14,
        horizontalalignment="center",
        verticalalignment="center",
        transform=axtitle.transAxes,
        bbox={"boxstyle": "square,pad=0.5", "ec": "k", "fc": "w"},
    )
    axes = [ax1, ax2, ax3, axcm, axtitle]
    img = ax1.pcolormesh(
        ns,
        ms,
        mapa,
        shading="nearest",
        cmap="magma",
        vmin=0.05 * mapa.max(),
        norm=norm,
        alpha=1,
        rasterized=True,
        linewidth=0,
        edgecolors="none",
    )
    fig.colorbar(img, cax=axcm, label="P [a.u]")
    # args = np.array(np.unravel_index(mapa.argmax(), mapa.shape))
    ax1.set_ylabel("m")
    ax1.xaxis.set_minor_locator(MultipleLocator(1))
    ax1.yaxis.set_minor_locator(MultipleLocator(1))
    ax1.xaxis.set_major_locator(MultipleLocator(5))
    ax1.yaxis.set_major_locator(MultipleLocator(5))
    ax1.xaxis.tick_top()
    ax1.xaxis.set_label_position("top")
    ax1.set_xlabel("n")
    ax1.tick_params(labelbottom=False)
    for idx, peak in enumerate(peaks):
        ax2.plot(ns, mapa[peak[0]], lw=(1 - idx / 10), zorder=(10 - idx))
        ax3.plot(mapa.T[peak[1]], ms, lw=(1 - idx / 10), zorder=(10 - idx))
        ax1.plot(ns[peak[1]], ms[peak[0]], "o", ms=5, mec="k")
    ax2.xaxis.set_minor_locator(MultipleLocator(1))
    ax2.xaxis.set_major_locator(MultipleLocator(5))
    ax2.grid(True, which="both", axis="x", ls="--", lw=0.5)
    ax2.set_ylim([0, 1.05 * mapa.max()])
    ax2.set_xlabel("n")
    ax2.set_ylabel("P [a.u]")
    ax3.grid(True, which="both", axis="y", ls="--", lw=0.5)
    ax3.yaxis.set_minor_locator(MultipleLocator(1))
    ax3.yaxis.set_major_locator(MultipleLocator(5))
    ax3.yaxis.set_label_position("right")
    ax3.yaxis.tick_right()
    ax3.set_xlim([0, 1.05 * mapa.max()])
    ax3.set_ylabel("m")
    ax3.invert_xaxis()
    ax3.set_xlabel("P [a.u]")
    return fig, axes


def clearfig(fig):
    axes = np.array(fig.get_axes()).flatten()
    for ax in axes:
        ax.cla()
    fig.clear()


def plotmapa_alone(mapa, ns, ms, norm=None, title="", fig=None, figsize=None):
    """
    Plots the 3D lomb periodogram, and optionally finds the points with maxima.
    """
    # mapa=mapa.T
    if fig is None:
        fig = plt.figure(
            figsize=figsize, constrained_layout=False, tight_layout=False, dpi=300
        )
    else:
        clearfig(fig)

    ax1 = fig.add_subplot()

    img = ax1.pcolor(
        ns,
        ms,
        mapa,
        # shading='nearest',
        cmap="magma",
        vmin=0.05 * mapa.max(),
        norm=norm,
        rasterized=True,
        # linewidth=0.01,
        # edgecolors='face'
    )
    cbar = fig.colorbar(img, ax=ax1, label="P [a.u]", format="%.1e")
    # args = np.array(np.unravel_index(mapa.argmax(), mapa.shape))
    ax1.set_ylabel("m")
    ax1.xaxis.set_minor_locator(MultipleLocator(1))
    ax1.yaxis.set_minor_locator(MultipleLocator(1))
    ax1.xaxis.set_major_locator(MultipleLocator(5))
    ax1.yaxis.set_major_locator(MultipleLocator(5))
    ax1.grid(which="major", color="w", lw=0.3, alpha=0.2, ls="--", zorder=1000)
    ax1.grid(which="minor", color="r", lw=0.1, alpha=0.5, ls="--", zorder=1000)

    ax1.set_xlabel("n")

    return fig, ax1
