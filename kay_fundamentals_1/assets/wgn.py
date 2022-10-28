from math import pi
from platform import python_implementation
from numpy import linspace, exp, sqrt
from matplotlib import pyplot

mu = 1
sigma = 1

x = linspace(-5, 5, 10000)
y = (1 / sqrt(2 * pi * (sigma**2))) * exp((-1 / (2 * (sigma**2))) * (x - mu)**2)

pyplot.plot(x, y, linewidth=2, color='b', label='PDF')
pyplot.axvline(mu, color='k', linewidth=2, label='Mean')
pyplot.grid(color='k', linestyle='--', linewidth=1)
pyplot.title('PDF of White Gaussian Noise')
pyplot.xlabel('x')
pyplot.ylabel('$\mathcal{P}${x; $\\theta, \sigma$}')
pyplot.legend()
pyplot.show()