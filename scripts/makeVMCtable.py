import sys
import os
import re

import numpy as np
import yaml

path = sys.argv[1]
tfname = sys.argv[2]
capfname = sys.argv[3]
label = sys.argv[4]
xsize = sys.argv[5]
ysize = sys.argv[6]

infoDict = {}
for fname in os.listdir(path):
    NIndex = fname.index("N")
    with open(path + "/" + fname, 'r') as inputFile:
        tmpDict = yaml.load(inputFile, Loader=yaml.CLoader)
        infoDict.setdefault(tmpDict["Const"],
                {}).setdefault(int(fname[NIndex+1:fname.find("_",NIndex)]),
                        float(tmpDict["Energy"]))
    # withopen inputFile
# end for fname

with open(tfname, "w") as tfile:
    nCount = len(infoDict[1.0].keys())
    tfile.write("\\begin{table}[H]\n    \\centering\scriptsize\n")
    tfile.write("\\caption{"+capfname+"}\n    \\label{tab:"+label+"}\n")
    tfile.write("   \\renewcommand*{\\arraystretch}{%s}\n" % xsize)
    tfile.write("   \\setlength{\\tabcolsep}{%spt}\n" % ysize)
    tfile.write("   \\begin{tabular}{"+"cc"+"".join(["c" for i in range(nCount + 1)])+"}\n")
    tfile.write("\\toprule\\hline $\\omega$ & \\multicolumn{%i}{c}{$N$} \\\\ \\hline\n" % nCount)
    for n in sorted(infoDict[1.0].keys()):
        tfile.write(" & " + "$" + str(n) + "$")
    tfile.write("\\\\\n")
    for w in sorted(infoDict.keys()):
        tfile.write("$"+str(w)+"$")
        for N in sorted(infoDict[w].keys()):
            tfile.write(" & $%.5f$" % infoDict[w][N])
        tfile.write("\\\\\n")
    tfile.write("\\hline\\bottomrule\\end{tabular}\n\\end{table}")
# end with open
