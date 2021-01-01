from xevo import eobj

from rndtrafos import trafos
import random
import numpy as np

class travo(eobj):
  """eobj transforming x and y to maximize linearity"""
  def __init__(s,x=None,y=None,hx=None,hy=None):
    s.initial()
    s.x=x
    s.y=y
    if hx is None:hx=[]
    if hy is None:hy=[]
    s.hx=hx
    s.hy=hy
  def _visx(s):
    return "-".join(s.hx)
  def _visy(s):
    return "-".join(s.hy)
  def __str__(s):
    return "X:"+s._visx()+" Y:"+s._visy()
  def __add__(a,b):
    x=[(a+b)/2 for a,b in zip(a.x,b.x)]
    y=[(a+b)/2 for a,b in zip(a.y,b.y)]
    return travo(x=x,y=y,hx=["mean("+a._visx()+"|"+b._visx()+")"],hy=["mean("+a._visy()+"|"+b._visy()+")"])

  
  def randomize(s):
    return s.mutate()
  def rndtrafo(s,x,o):
    q=random.choice(trafos)
    return q["n"],q["q"](x,o)
  def mutate(s):
    x,y=[q for q in s.x],[q for q in s.y]
    hx=[q for q in s.hx]
    hy=[q for q in s.hy]
    if random.random()<0.5:
      tx,x=s.rndtrafo(x,y)
      hx.append(tx)
    else:
      ty,y=s.rndtrafo(y,x)
      hy.append(ty)
    return travo(x,y,hx,hy)
    
    
  def calcstrength(s):
    ret= np.corrcoef(s.x,s.y)[1,0]
    if np.isnan(ret):return -2
    return ret
  def _copy(s):
    return travo([q for q in s.x],[q for q in s.y],[q for q in s.hx],[q for q in s.hy])