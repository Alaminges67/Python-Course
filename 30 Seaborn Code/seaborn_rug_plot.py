import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.rugplot(data["total_bill"])
plt.show()