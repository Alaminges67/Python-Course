import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.ecdfplot(data["total_bill"], stat="proportion")
plt.show()