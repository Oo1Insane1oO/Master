import sys
import os

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
                        {}).setdefault(tmpDict["numparticles"], tmpDict["E0"])
    # withopen inputFile
# end for fname

Nval = sorted(infoDict[next(iter(infoDict))][1].keys())
print Nval

for wk in sorted(infoDict.keys()):
    for Lk in sorted(infoDict[wk].keys()):
        for nval in Nval:
            if nval not in infoDict[wk][Lk]:
                infoDict[wk][Lk][nval] = "-"

print infoDict[0.1][6][20]

# with open(wfile, "w") as ofile:
#     nCount = infoDict[next(iter(infoDict))].count()
#     oFile.write("\\begin{table}[H]\n    \\centering")
#     oFile.write("   \\caption{Results}\n    \label{label}")
#     oFile.write("   \\begin{tabular}{"+"".join("l" for i in range(nCount) + 2))+"}\n"
#     for wkey in sorted(infoDict.keys()):
#         oFile.write("\\multirow{%i}{*}{}\n" % nCount)
#         for Nkey in sorted(infoDict[wkey].keys()):
#             for Lkey in sorted(infoDict[wkey][Nkey].keys()):
#                 oFile.write(str(infoDict[wkey][Nkey][Lkey]) + " & ")
