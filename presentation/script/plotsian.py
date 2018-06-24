import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.special import jv

def sian(M, f, x0, Tmax=100., nstd=0.2):
    x = np.linspace(-2,2,10000)

    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x,f(x))
    ax.autoscale(enable=False, axis='both')
    ax.set_xlim(-2,2)
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)

    fig.canvas.draw()

    bg = fig.canvas.copy_from_bbox(ax.bbox)
        
    plt.savefig("data/fig0.png")

    xold = x0
    T = Tmax
    for i in range(1,M):
        xnew = np.random.normal(xold, nstd)

        if np.exp(-(f(xnew) - f(xold))/T) >= np.random.uniform():
            if (np.abs(xnew) <= 2):
                xold = xnew
        T = Tmax/i

        newp = ax.plot(xold, f(xold), 'ro', markersize=3.0)[0]
        ax.set_title("T = " + str(T))

        fig.canvas.blit(ax.bbox)
        fig.canvas.flush_events()

        if (i%100) == 0:
            plt.savefig("data/fig%i.png" % i)

        newp.remove()

    return xold, f(xold)

f = lambda x: scipy.signal.chirp(x, 0.5,1, 2)*np.cos(x) * (0 if np.abs(x > 2).all() else 1)

# xm, fm = sian(100000, ackelyn, (-0.01,0.01), 50.)
xm, fm = sian(10000, f, -1.0, 1000., 0.5)

print xm, fm
