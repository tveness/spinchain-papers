#!/usr/bin/python

from os import system
import numpy as np


for et in np.arange(-0.66,-0.5,.01):
    print(f"Fitting for e: {et}")
    system(f"sc --rot-frame {et}")

    
        

