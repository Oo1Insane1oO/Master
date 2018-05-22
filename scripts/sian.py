import numpy as np

def sian(M, f, x0):
    xold = np.array(x0)
    Tmax = 100.
    T = Tmax
    for i in range(1,M):
        xnew = np.random.normal(xold, 1.0)

        if np.exp(-(f(xnew) - f(xold))/T) >= np.random.uniform():
            xold = xnew
        T = Tmax/i

    return xold, f(xold)

ackelyn = lambda x: -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2+x[1]**2))) -\
        np.exp(0.5*(np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))) +\
        20+np.exp(1)

rastrigin = lambda x: 20 + x[0]**2 - 10*np.cos(2*np.pi*x[0]) + x[1]**2 - \
        10*np.cos(2*np.pi*x[1])

# xm, fm = sian(100000, ackelyn, (-0.01,0.01))
xm, fm = sian(100000, rastrigin, (-0.01,0.001))

#     np.random.seed(2)
#     np.random.seed(2)

print xm, fm
