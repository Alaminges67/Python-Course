import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", size="size", hue="day", data=data, sizes=(20, 200))
plt.show()