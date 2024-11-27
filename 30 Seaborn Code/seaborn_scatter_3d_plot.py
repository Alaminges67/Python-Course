import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns; import numpy as np
data = sns.load_dataset("iris")
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(data["sepal_length"], data["sepal_width"], data["petal_length"], c="blue", marker="o")
plt.show()