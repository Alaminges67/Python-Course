import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris").iloc[:, :-1].corr()
sns.heatmap(data, cmap="coolwarm", center=0, annot=True)
plt.show()