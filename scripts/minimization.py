import numpy as np
import matplotlib.pyplot as plt

def minimize(M, eta, f, df, x0):
    x = np.zeros((M,2)) 
    x[0] = x0
    fv = np.zeros(M)
    fv[0] = f(x[0])
    for i in range(1,M):
        x[i] = x[i-1] - eta * df(x[i-1])
        fv[i] = f(x[i])

    return x, fv

rosenbrock = lambda x: 100 * (x[1] - x[0]**2)**2 + (x[0] - 1)**2
drosenbrock = lambda x: np.array([-400*x[0]*(x[1] - x[0]**2) + 2*(x[0] - 1),
    200*(x[1] - x[0]**2)])

sphere = lambda x: sum([x[i]**2 for i in range(len(x))])
dsphere = lambda x: 2*np.array([x[i] for i in range(len(x))])

eta = 0.0001
M = 100000

x, fv = minimize(M, eta, rosenbrock, drosenbrock, (0,0.5))
# x, fv = minimize(M, eta, sphere, dsphere, (5,5))
print x[-1], fv[-1]

plt.plot(np.arange(0,M), fv)
plt.show()
