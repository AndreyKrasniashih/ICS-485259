from numpy import*
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab
import pylab

name = str(input())
def count_sign():
    symbols=["?", '.', ',', ';']
    for i in range(0, len(symbols)):
        xdata=[symbols[i]]
        ydata=[name.count(symbols[i])]
        pylab.bar(xdata, ydata)

    pylab.show()
count_sign()         