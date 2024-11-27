import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="day")
g.map(sns.stripplot, "time", "total_bill")
plt.show()