import numpy as df
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#This will be the function that returns the ODE

def model  (y, t, p):

    #part 1 of the equation
    s = 1/((1-p) + (p/y))
    #the equation after its last derivative
    s1 = (p / (y * y)) * (s * s)
    return s1
#setting our y variable
y0 = .9
#creating the line spacing in our graph
t = df.linspace(0, 2048)
p0 = .1
#these are the 3 different version that solve our ODE
run1 = odeint(model, y0, t, args=(p0,))
p0 = .2
run2 = odeint(model, y0, t, args=(p0,))
p0 = .5
run3 = odeint(model, y0, t, args=(p0,))
#This where we plot our results
plt.plot(t, run1, 'r--', label='.1')
plt.plot(t, run2, 'g--', label='.2')
plt.plot(t, run3, 'b--', label='.3')
#This is editing our graph and all its labels
plt.xlabel('Number of Cores')
plt.ylabel('Speed up')
plt.legend(loc='upper left')
plt.title('Amdahls Law')
plt.show()