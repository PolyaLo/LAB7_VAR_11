import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
# функция
y_1 = lambda x: np.sinc(x)
y_2 = lambda x: np.sinc(x / np.pi)
fig, ax = plt.subplots()
ax.set_xticks([-20, -15, -10, -5, 0, 5, 10, 15, 20])
ax2 = ax.twiny()
ax2.set_xticks([-6*np.pi, -4*np.pi, -2*np.pi, 0, 2*np.pi, 4*np.pi, 6*np.pi])
ax2.set_xticklabels([r"$-6\pi$", r"$-4\pi$", r"$-2\pi$","$0$", r"$2\pi$",
                    r"$4\pi$", r"$6\pi$"])
x = np.linspace(-20, 20, 200)
plt.plot(x, y_1(x), label=r'$\frac{\sin(x\pi)}{x\pi}$', color='blue')
plt.plot(x, y_2(x), label=r'$\frac{\sin(x)}{x}$', color='red')
plt.legend()
ax.grid(which='major',
        color='blue')
ax2.grid(which='major',
         color='red')
ax.minorticks_on()
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.minorticks_on()
plt.show()
