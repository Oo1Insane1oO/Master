import sys
import os
import operator

import numpy as np
import matplotlib.pyplot as plt
import yaml

path = sys.argv[1]
dim = sys.argv[2]
xlen = float(sys.argv[3])

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

wkey = 1.0
ftsize=14
fig, ax = plt.subplots(len(Nval), 1)
fig.set_figwidth(xlen)
fig.text(0.085, 0.5, "Ground state energy", ha='center', va='center', rotation='vertical', fontsize=ftsize)
ax[0].set_title("$\omega=%.2f$" % wkey, fontsize=ftsize)
for i,n in enumerate(Nval):
    tmpVals = []
    lKeys = sorted(infoDict[wkey].keys())
    for lk, lkey in enumerate(lKeys):
        tmpVals.append(infoDict[wkey][lkey][n])
        
    ax[i].tick_params(axis='x', bottom=False, labelbottom=False)

    ax[i].set_xlim([lKeys[0], lKeys[-1]])

    if i <= 1:
        ax[i].plot(lKeys[n/2-1:], tmpVals[n/2-1:], '-o', markersize=2.0, label="$N=%i$" % n)
    else:
        ax[i].plot(lKeys[n/2:], tmpVals[n/2:], '-o', markersize=2.0, label="$N=%i$" % n)
    ax[i].legend()

ax[-1].tick_params(axis='x', bottom=True, labelbottom=True)
ax[-1].set_xticks(sorted(infoDict[wkey]))
ax[-1].set_xlabel("Number of basis functions", fontsize=ftsize)

plt.savefig("D" + dim + "_DW.pdf", dpi=300)

plt.show()
