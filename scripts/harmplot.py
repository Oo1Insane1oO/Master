import numpy as np
import matplotlib.pyplot as plt

hof = lambda x: 0.5*x**2

x = np.linspace(-10,10, 10000)
plt.plot(x, hof(x))
plt.ylabel('$\\frac{1}{2}m\\omega x^2$')
plt.xlabel('x')
plt.show()
