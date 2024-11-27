import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.errorbar(data["total_bill"], data["tip"], yerr=0.2, fmt="o", color="gray", alpha=0.5)
plt.show()