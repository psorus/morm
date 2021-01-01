import math
import numpy as np



trafos=[
        {"n":"sin","q":lambda x,o:np.sin(x)},
        {"n":"cos","q":lambda x,o:np.cos(x)},
        {"n":"tan","q":lambda x,o:np.tan(x)},
        {"n":"sinh","q":lambda x,o:np.sinh(x)},
        {"n":"cosh","q":lambda x,o:np.cosh(x)},
        {"n":"tanh","q":lambda x,o:np.tanh(x)},
        {"n":"asin","q":lambda x,o:np.arcsin(x)},
        {"n":"acos","q":lambda x,o:np.arccos(x)},
        {"n":"atan","q":lambda x,o:np.arctan(x)},
        {"n":"asinh","q":lambda x,o:np.arcsinh(x)},
        {"n":"acosh","q":lambda x,o:np.arccosh(x)},
        {"n":"atanh","q":lambda x,o:np.arctanh(x)},
        {"n":"exp","q":lambda x,o:np.exp(x)},
        {"n":"log","q":lambda x,o:np.log(x)},
        {"n":"divide","q":lambda x,o:[xx/oo for xx,oo in zip(x,o)]},
        {"n":"abs","q":lambda x,o:np.abs(x)},
        {"n":"sqrt","q":lambda x,o:[q**0.5 for q in x]},
        {"n":"square","q":lambda x,o:[q**2.0 for q in x]},



       ]



