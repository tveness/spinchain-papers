#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import root
# Define functions required for finite-size histogram
def f(z):
    return -np.log(np.sinh(z)/z) / z

def fp(z):
    return (1-z/np.tanh(z) + np.log(np.sinh(z)/z))/z**2

def fpp(z):
    return (z**2/np.sinh(z)**2 + 2*z/np.tanh(z) -2.0*np.log(np.sinh(z)/z) - 3.0)/z**3

def g(z,e):
    return (beta - z)*f(beta-z) + e*z

def gp(z,e):
    return e - f(beta-z) - (beta-z)*fp(beta-z)

def gpp(z,e):
    return (beta-z)*fpp(beta-z)+2*fp(beta-z)

def eps(z):
    return 1/z - 1.0/np.tanh(z)

# Define parameters
e_target = -0.66
ell=39

# Calculate beta for isotropic ensemble and target energy
beta = root(lambda z: eps(z) -e_target,1).x[0]
print("beta: ",beta)
#Generate grid for energy
de=0.001
e_arr = np.arange(-0.9001,-0.4001,de)
p_arr = [ee for ee in e_arr]
#Calculate probability distribution
for i,ee in enumerate(e_arr):
    zstar = root(gp,1,args=(ee)).x[0]
#    print(zstar,gpp(zstar,ee))
    P = np.exp(-ell*g(zstar,ee))/np.sqrt(-ell*gpp(zstar,ee)) 
    p_arr[i] = P
#Normalise
N = sum(p_arr)*de
p_arr = p_arr / N

plt.plot(e_arr,p_arr)
plt.xlabel("e")
plt.ylabel("P(e)")
plt.show()
# Save to file
ep = list(zip(e_arr,p_arr))
np.savetxt("analytic-hist.dat",ep)
