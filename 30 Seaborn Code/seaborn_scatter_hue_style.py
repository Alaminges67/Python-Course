import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", hue="day", style="time", data=data)
plt.show()