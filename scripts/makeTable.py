import sys
import os
import operator

import pandas as pd
import numpy as np
import yaml

path = sys.argv[1]
wfile = sys.argv[2]
    
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

with open(wfile, "w") as ofile:
    nCount = len(Nval)
    ofile.write("\\begin{table}[H]\n    \\centering")
    ofile.write("   \\caption{Results}\n    \label{label}")
    ofile.write("   \\begin{tabular}{"+"".join("l" for i in range(nCount + 2))+"}\n")
    ofile.write("\\multicolumn{1}{c}{w} & L & N & " + "".join([str(n) + "& " for n in Nval]) + "\\\\\n")
    for wkey in sorted(infoDict.keys()):
        for lk, Lkey in enumerate(sorted(infoDict[wkey].keys())):
            for i,n in enumerate(Nval):
                if (lk==0) and (i==0):
                    ofile.write("\\multirow{%i}{*}{%.3f} & " % (Lmax, float(wkey)))
                # end if
                if lk!=0 and i==0:
                    try:
                        ofile.write("%i & %f & " % (Lkey, infoDict[wkey][Lkey][n]))
                    except:
                        ofile.write("%i & %s & " % (Lkey, infoDict[wkey][Lkey][n]))
                    # end trye
                # end if
                try:
                    ofile.write("%f & " % infoDict[wkey][Lkey][n])
                except:
                    ofile.write("%s & " % infoDict[wkey][Lkey][n])
                # end trye
            # end forn
            ofile.write(" \\\\\n")
        # end forenum lk, Lkey
    # end forwkey
    ofile.write("\\end{tabular}\n\\end{table}")
# end withopen ofile
