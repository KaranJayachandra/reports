from matplotlib import pyplot
from numpy import linspace

x = linspace(0, 10, 100)
y_1 = 0.5 * x
y_2 = 0.5 * x + 5

z_1 = 0.5 * x
z_2 = -0.5 * x + 5

f, (ax1, ax2) = pyplot.subplots(1, 2, sharey=True)
ax1.plot(x, y_1, label='$\hat{\\theta_1}$')
ax1.plot(x, y_2, label='$\hat{\\theta_2}$')
ax1.grid()
ax1.set_xlabel('$\\theta$')
ax1.set_ylabel('var ($\hat{\\theta}$)')
ax2.plot(x, z_1, label='$\hat{\phi_1}$')
ax2.plot(x, z_2, label='$\hat{\phi_2}$')
ax2.grid()
ax2.set_xlabel('$\phi$')
ax2.set_ylabel('var ($\hat{\phi}$)')
pyplot.suptitle('MVU Estimators')
pyplot.show()