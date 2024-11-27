import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("titanic")
sns.histplot(data=data, x="class", hue="sex", multiple="stack")
plt.show()