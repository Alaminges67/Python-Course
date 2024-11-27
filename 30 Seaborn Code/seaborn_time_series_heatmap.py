import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights").pivot("month", "year", "passengers")
sns.heatmap(data, cmap="YlGnBu")
plt.show()