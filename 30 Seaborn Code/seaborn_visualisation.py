import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
data = sns.load_dataset("tips")

# 1. Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 2. Line Plot
plt.figure(figsize=(8, 6))
sns.lineplot(x="size", y="total_bill", data=data)
plt.title("Line Plot of Size vs Total Bill")
plt.xlabel("Size")
plt.ylabel("Total Bill")
plt.show()

# 3. Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data["total_bill"], kde=True)
plt.title("Histogram of Total Bill with KDE")
plt.xlabel("Total Bill")
plt.show()

# 4. Bar Plot
plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=data, estimator=sum)
plt.title("Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill (Sum)")
plt.show()

# 5. Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 6. Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x="day", y="total_bill", data=data)
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 7. Pair Plot
sns.pairplot(data[["total_bill", "tip", "size"]])
plt.suptitle("Pair Plot of Total Bill, Tip, and Size", y=1.02)
plt.show()

# 8. Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 9. Count Plot
plt.figure(figsize=(8, 6))
sns.countplot(x="day", data=data)
plt.title("Count of Days")
plt.xlabel("Day")
plt.show()

# 10. Strip Plot
plt.figure(figsize=(8, 6))
sns.stripplot(x="day", y="total_bill", data=data)
plt.title("Strip Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()