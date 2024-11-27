import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11)
y1 = np.random.randint(1, 10, size=10)
y2 = np.random.randint(1, 10, size=10)
y3 = np.random.randint(1, 10, size=10)
plt.stackplot(x, y1, y2, y3, labels=["A", "B", "C"], alpha=0.6)
plt.legend(loc="upper left")
plt.show()