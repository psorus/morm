

import xevo
from travo import *
from trivmute import *

import math
import numpy as np

import matplotlib.pyplot as plt


def f(x):return x**2+np.exp(x)


sigma=0.03
x=[i/10 for i in range(100)]
y=[f(xx)+np.random.normal(0,sigma,1)[0] for xx in x]
# y=[3*xx+np.random.normal(0,sigma,1)[0] for xx in x]






genetics=trivmute()
genetics=xevo.crossevo()
obj=travo(x=x,y=y)#,sigma=sigma)

goalstrength=0.995
maxsteps=10000000

def runone(show=True):
  global c
  c=xevo.erun(genetics.copy(),obj,show=show,population=20,delay=0.001)
  c.run(goalstrength=goalstrength,maxsteps=maxsteps)

runone()

win=c.getwinner()
print(win)

# c.show_history(log=False)

plt.close()
plt.plot(win.x,win.y)
plt.xlabel(win._visx())
plt.ylabel(win._visy())
plt.show()


