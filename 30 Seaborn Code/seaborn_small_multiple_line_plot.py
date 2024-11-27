import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
g = sns.FacetGrid(data, col="month", col_wrap=4, height=2.5)
g.map(sns.lineplot, "year", "passengers")
plt.show()