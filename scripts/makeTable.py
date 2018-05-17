import sys
import os

import numpy as np
import yaml

path = sys.argv[1]
# wfile = sys.argv[2]
    
infoDict = {}
for f in os.listdir(path):
    tmpDict = yaml.load(file(path + "/" + f, 'r'))
    del tmpDict["coeffs"]
    infoDict.setdefault(tmpDict["omega"],
            {}).setdefault(tmpDict["numparticles"],
                    {}).setdefault(tmpDict["numbasis"], tmpDict["E0"])

print infoDict[0.1][2][15]

