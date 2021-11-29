from numpy import*
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab

text = str(input())

def count_letters():
    alphabet = ['й', 'ц', 'у', 'к', 'е',\
                'и', 'р', 'п', 'щ', 'н',\
                'с', 'о', 'а', 'ф', 'г',\
                'д', 'л', 'в', 'і', 'ш'\
                ]
    for i in renge(0, len(albhabet)):
        xdata = [albhabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
    count_letters()    
        