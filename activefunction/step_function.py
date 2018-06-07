import numpy as np
import matplotlib.pylab as plt

def step_func(x):
    y = x > 0
    return y.astype(int)

if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_func(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
