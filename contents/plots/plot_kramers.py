import matplotlib.pyplot as plt
import numpy as np


plt.style.use("ggplot")


def f(x):
    return -np.log(1.0 * np.exp(-(x**2)) + 1.2 * np.exp(-((x - 2) ** 2)))


x = np.linspace(-1, 3)

plt.plot(x, f(x))

import tikzplotlib

tikzplotlib.save("plot_kramers.tex")
