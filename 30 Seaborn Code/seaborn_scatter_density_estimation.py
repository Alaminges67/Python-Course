import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.kdeplot(x=data["sepal_length"], y=data["sepal_width"], cmap="Blues", fill=True)
plt.scatter(data["sepal_length"], data["sepal_width"], color="orange", s=5)
plt.show()