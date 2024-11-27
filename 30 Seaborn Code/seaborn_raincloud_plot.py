import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=data)
sns.stripplot(x="day", y="total_bill", hue="sex", data=data, dodge=True, color="gray", alpha=0.5)
plt.show()