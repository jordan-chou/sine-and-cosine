#   Jordan Chou
#   Dec. 18, 2019
#   Plotting the graphs of sin and cos

import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-360, 360, 200)
plt.plot(x, np.sin(x*np.pi/180))
plt.plot(x, np.cos(x*np.pi/180))
plt.xlabel("Angle [degrees]")
plt.ylabel("Amplitude")
plt.xticks(np.arange(-360, 360+1, 180))
plt.axis("tight")
plt.show()
