import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
data = pd.read_csv("sales_data.csv")

print(data)

# Style
sns.set_theme()

# Sales Trend Line Chart
plt.figure(figsize=(8,5))
plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Profit Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(x="Month", y="Profit", data=data)
plt.title("Monthly Profit Analysis")
plt.show()

# Sales Distribution Histogram
plt.figure(figsize=(8,5))
plt.hist(data["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(data[["Sales","Profit"]].corr(),
            annot=True,
            cmap="Blues")
plt.title("Correlation Between Sales and Profit")
plt.show()