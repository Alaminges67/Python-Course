import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("flights")
sns.lineplot(x="month", y="passengers", hue="year", data=data)
plt.show()