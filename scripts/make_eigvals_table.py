import os
import sys

import numpy as np

path = sys.argv[1]
filename = sys.argv[2]
capfname = sys.argv[3]
label = sys.argv[4]
xsize = sys.argv[5]
ysize = sys.argv[6]

Ldict = {}
for fname in os.listdir(path):
    values = map(float, open(path + "/" + fname).read().split())
    Ldict[int(fname[fname.find('L')+1:fname.find('t')-1])] = values

keysSorted = sorted([k for k in Ldict.keys()])
valuesSorted = [Ldict[key] for key in keysSorted]

for i in range(len(valuesSorted)):
    for j in range(len(valuesSorted[-1]) - len(valuesSorted[i])):
        valuesSorted[i].append("-");

with open(filename, "w") as ofile:
    ofile.write("\\begin{table}[H]\n    \\centering\\footnotesize\n")
    ofile.write("\\input{"+capfname+"}\n    \\label{tab:"+label+"}\n")
    ofile.write("\\scalebox{" + xsize + "}[" + ysize + "]{%\n")
    ofile.write("   \\begin{tabular}{"+"".join(["c" for i in range(len(keysSorted))])+"}\n")
    ofile.write("L") 
    for k in keysSorted:
        ofile.write(" & %i" % k)
    ofile.write("\\\\\n")
    for i,value in enumerate(valuesSorted):
        for j,v in enumerate(value):
            if i==0 and j==0:
                ofile.write("\\multirow{%i}{*}{}" % len(keysSorted))
            # end if
            try:
                ofile.write(" & %.5f" % v)
            except:
                ofile.write(" & %s" % v)
        # end forjv
        ofile.write("\\\\\n")
    # end forivalue
    ofile.write("\\hline\\bottomrule\\end{tabular}%\n}\n\\end{table}")
# end withopen
