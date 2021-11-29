import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

x = np.linspace(0, 4, 100)
y = 5*np.sin(10*x)*np.sin(3*x)

ax.plot(x, y)
plt.show()
