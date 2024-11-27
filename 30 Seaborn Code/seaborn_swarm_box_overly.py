import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data, color="white")
sns.swarmplot(x="day", y="total_bill", data=data, color=".25")
plt.show()