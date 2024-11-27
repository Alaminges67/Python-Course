import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.kdeplot(x="total_bill", hue="time", data=data, fill=True)
plt.show()