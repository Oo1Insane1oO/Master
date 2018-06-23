import sys
import os
import operator

import numpy as np
import matplotlib.pyplot as plt
import yaml

path = sys.argv[1]
dim = sys.argv[2]

infoDict = {}
for fname in os.listdir(path):
    with open(path + "/" + fname, 'r') as inputFile:
        tmpDict = yaml.load(inputFile, Loader=yaml.CLoader)
        del tmpDict["coeffs"]
        infoDict.setdefault(tmpDict["omega"],
                {}).setdefault(tmpDict["numbasis"],
                        {}).setdefault(tmpDict["numparticles"], float(tmpDict["E0"]))
    # withopen inputFile
# end for fname

Nval = sorted(set(reduce(operator.add, [l.keys() for l in
    infoDict[next(iter(infoDict))].values()])))
Lmax = len(infoDict[next(iter(infoDict))].keys())

for wk in sorted(infoDict.keys()):
    for Lk in sorted(infoDict[wk].keys()):
        for nval in Nval:
            if nval not in infoDict[wk][Lk]:
                infoDict[wk][Lk][nval] = "-"

for i,n in enumerate(Nval):
    fig, ax = plt.subplots(len(infoDict.keys()), 1)
    fig.text(0.05, 0.5, "Ground state energy", ha='center', va='center', rotation='vertical')
    ax[0].set_title("Number of particles: $%i$" % n)
    for w, wkey in enumerate(sorted(infoDict.keys())):
        tmpVals = []
        lKeys = sorted(infoDict[wkey].keys())
        for lk, lkey in enumerate(lKeys):
            tmpVals.append(infoDict[wkey][lkey][n])
        ax[w].tick_params(axis='x', bottom=False, labelbottom=False)
        ax[w].plot(lKeys[i:], tmpVals[i:], '-o', markersize=2.0, label="$\\omega=%.2f$" % wkey)
        ax[w].legend()

    ax[-1].tick_params(axis='x', bottom=True, labelbottom=True)
    ax[-1].set_xticks(sorted(infoDict[wkey])[i:])
    ax[-1].set_xlabel("Number of basis functions")

    plt.savefig("N" + str(n) + "_D" + dim + ".pdf", dpi=300)

plt.show()
