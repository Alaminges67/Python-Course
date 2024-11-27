import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.swarmplot(x="day", y="total_bill", data=data)
plt.show()