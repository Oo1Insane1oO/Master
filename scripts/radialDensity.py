import sys

import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1]

radialMatrix = np.loadtxt(fname)

surf = plt.imshow(radialMatrix, origin='lower')
plt.show()
