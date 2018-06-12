regio = []
peaks_sample = []
peaks_base = []

with open('M18-0001.MSI.txt') as f:
    for x, line in enumerate(f):
        line = line.strip().split('\t')
        if x != 0:
            regio.append(line[0]) 
            peaks_sample.append(float(line[3]))

with open('MSI_BASELINE.txt') as b:
    for x, line in enumerate(b):
        line = line.strip().split('\t')
        if x !=0:
            peaks_base.append(float(line[2]))

import matplotlib.pyplot as plt
import numpy as np

xpos = np.arange(len(regio))

plt.bar(xpos-0.2,peaks_sample, width =0.4,label="Patient")
plt.bar(xpos+0.2,peaks_base, width =0.4,label="Baseline")

plt.xticks(xpos,regio, rotation=10,fontsize=4)
plt.ylabel("Aantal pieken")
plt.xlabel("Loci")
plt.title('Pieken per loci: Patient vs Baseline', fontsize = 20)
plt.legend()

plt.savefig('test.png')
