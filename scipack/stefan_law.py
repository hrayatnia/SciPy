__author__ = 'rayatnia'
#constants table
import scipy.constants.constants as cn
#numberical
import numpy as np
#ploting
import matplotlib.pyplot as plot

Asphalt_e=0.88

def J(T):
    return cn.Stefan_Boltzmann*Asphalt_e*(T)**4


array=np.linspace(0,550,num=550)

y=[]
x=[]
for element in array:
    x.append(element)
    y.append(J(element))

plot.plot(x,y)
plot.savefig('Stefan_bolt_fig.eps')