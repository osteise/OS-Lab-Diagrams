import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Put data here
data = [5, 10, 5, 9, 7, 10, 10, 10, 8, 5]
data1 = [8, 8, 10, 7, 10, 10, 10, 10, 10, 10]

# Convert data into a pandas DataFrame
df = pd.DataFrame(data, columns=["values"])
df_values = df["values"]

df1 = pd.DataFrame(data1, columns=["values"])
df1_values = df1["values"]

# Calculate mean and standard deviation
mean = df_values.mean()
std = df_values.std()

mean1 = df1_values.mean()
std1 = df1_values.std()

# Plot a histogram
plt.hist(df_values, bins=5, density=True, alpha=0.5, color="blue", edgecolor="black", label="Original")
plt.hist(df1_values, bins=5, density=True, alpha=0.5, color="green", edgecolor="black", label="Modified")

# Create range of x values (bell curve)
x = np.linspace(df_values.min(), df_values.max())

# Plot a bell curve using data's mean and std
plt.plot(x, stats.norm.pdf(x, mean, std), color='black', label="Original Normal Distribution")
plt.plot(x, stats.norm.pdf(x, mean1, std1), color='red', label="Modified Normal Distribution")

# Add titles, labels, legend and grid
plt.title("Bell Curve of Process Data")
plt.xlabel("Successful Process Deadline")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("bell_curve.png")
plt.show()