# import numpy as np
# import matplotlib.pyplot as plt
# 
# hof = lambda x: 0.5*x**2
# 
# x = np.linspace(-10,10, 10000)
# plt.plot(x, hof(x))
# plt.ylabel('$\\frac{1}{2}m\\omega x^2$', fontsize=15)
# plt.xlabel('x', fontsize=15)
# 
# plt.savefig('HO1Dplot.pdf')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

R = 2.0
dwf = lambda x: 0.5 * (x**2 - 2*R*np.abs(x)+R**2)

x = np.linspace(-5,5, 10000)
plt.plot(x, dwf(x))
plt.ylabel('$\\frac{1}{2}m\\omega(x^2-2|x|+R^2$', fontsize=15)
plt.xlabel('x', fontsize=15)

plt.savefig('DW1Dplot.pdf')
plt.show()
