import pandas as pd
import numpy as np

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

if len(sys.argv)<4:
  print("usage: py show_slot.py slot_data.out nrb symbol_size")
  quit()

fname = sys.argv[1]
nrb = int(sys.argv[2])
symbol_size = int(sys.argv[3])

#nrb = 25
nre = 12
#symbol_size = nrb * nre  

v = np.fromfile(fname, dtype=np.short).reshape((-1,2))
c = np.array([complex(*x) for x in v])

c = c.reshape((-1, symbol_size ))
nsymb = c.shape[0]

symbols = range(0, nsymb)
prbs = range(0, nrb)
r = np.empty((nrb, nsymb))
for s in symbols:
  for prb in prbs:
    res = 0
    for re in range(0, nre ):
      if (c[s, re+(prb * nre)]!=0):
        res = 10
        
    r[prb, s]=res

#print(r)

fig, ax = plt.subplots()

im = ax.imshow(r)
ax.set_aspect('auto')
ax.set_xticks(np.arange(len(symbols)), labels=range(1,nsymb+1))
ax.set_ylim(-1, nrb+1)
ax.set_xlabel('Symbols')
ax.set_ylabel('PRBs')
fig.tight_layout()


plt.show()
