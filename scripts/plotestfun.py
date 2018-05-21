import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def plotfsurf(N, f, xmin, xmax):
    N = 100
    x = np.linspace(xmin,xmax,N)
    X,Y = np.meshgrid(x,x)

    fval = f((X,Y))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    plt.gca().patch.set_facecolor('white')

    surf1 = ax.plot_surface(X,Y,fval, cmap=cm.jet, antialiased=True)
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.1e'))

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    ax.tick_params(axis='z', which='major', pad=10)

    ax.set_xlabel('$x$', fontsize=11)
    ax.set_ylabel('$y$', fontsize=11)
    ax.set_zlabel('f(x,y)', labelpad=15, fontsize=11)

    plt.show()

if __name__ == "__main__":
    rosenbrock = lambda x: sum([100*(x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i
        in range(len(x)-1)])

    sphere = lambda x: sum([x[i]**2 for i in range(len(x))])

    plotfsurf(100000 , rosenbrock, -10, 10)
#     plotfsurf(100000, sphere, -10, 10)
    
