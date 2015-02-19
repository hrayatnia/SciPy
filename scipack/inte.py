from scipy.integrate import quad
import numpy as np
def f(x):
    return np.cos(np.exp(x))**2
x,error=quad(f,0,3)
print (x,error,sep="\t")