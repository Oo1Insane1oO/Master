import sys
import os
import operator

import pandas as pd
import numpy as np
import yaml

path = sys.argv[1]
wfile = sys.argv[2]
capfname = sys.argv[3]
label = sys.argv[4]
xsize = sys.argv[5]
ysize = sys.argv[6]

infoDict = {}
for fname in os.listdir(path):
    with open(path + "/" + fname, 'r') as inputFile:
        tmpDict = yaml.load(inputFile, Loader=yaml.CLoader)
        if tmpDict["I"] > 400:
            print tmpDict["I"], fname
        del tmpDict["coeffs"]
        infoDict.setdefault(tmpDict["omega"],
                {}).setdefault(tmpDict["numbasis"],
                        {}).setdefault(tmpDict["numparticles"], float(tmpDict["E0"]))
    # withopen inputFile
# end for fname

exit(1)

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
    ofile.write("\\begin{table}[H]\n    \\centering\scriptsize\n")
    ofile.write("\\input{"+capfname+"}\n    \\label{tab:"+label+"}\n")
    ofile.write("\\scalebox{" + xsize + "}[" + ysize + "]{%\n")
    ofile.write("   \\begin{tabular}{"+"cc|"+"".join(["c" for i in range(2,nCount + 2)])+"}\n")
    ofile.write("\\toprule\\hline\\multicolumn{2}{l|}{} & \\multicolumn{%i}{c}{$N$} \\\\ \\hline\n" % nCount)
    ofile.write("\\multicolumn{1}{c}{$\\omega$} & $L$ " + "".join([" & $" + str(n) + "$" for n in Nval]) + "\\\\\n")
    for wkey in sorted(infoDict.keys()):
        for lk, Lkey in enumerate(sorted(infoDict[wkey].keys())):
            for i,n in enumerate(Nval):
                if (lk==0) and (i==0):
                    ofile.write("\\hline\\multicolumn{1}{l|}{\\multirow{%i}{*}{$%.2f$}} & $%i$ & " % (Lmax, float(wkey), Lkey))
                # end if
                if (i==0) and (lk!=0):
                    try:
                        ofile.write("\\multicolumn{1}{l|}{} & $%i$ & $%.6f$ & " % (Lkey, infoDict[wkey][Lkey][n]))
                    except:
                        ofile.write("\\multicolumn{1}{l|}{} & $%i$ & $%s$ & " % (Lkey, infoDict[wkey][Lkey][n]))
                    # end trye
                elif i==(nCount-1):
                    try:
                        ofile.write("$%.6f$" % infoDict[wkey][Lkey][n])
                    except:
                        ofile.write("$%s$" % infoDict[wkey][Lkey][n])
                else :
                    try:
                        ofile.write("$%.6f$ & " % infoDict[wkey][Lkey][n])
                    except:
                        ofile.write("$%s$ & " % infoDict[wkey][Lkey][n])
                    # end trye
                # end if
            # end forn
            ofile.write(" \\\\\n")
        # end forenum lk, Lkey
    # end forwkey
    ofile.write("\\hline\\bottomrule\\end{tabular}%\n}\n\\end{table}")
# end withopen ofile
