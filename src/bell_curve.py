import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Put data here
data = [9, 10, 8, 7, 8, 9, 10, 9, 10, 10]

# Convert data into a pandas DataFrame
df = pd.DataFrame(data, columns=["values"])
df_values = df["values"]

# Calculate mean and standard deviation
mean = df_values.mean()
std = df_values.std()

# Plot a histogram
plt.hist(df_values, bins=5, density=True, alpha=0.8, color="lightblue", edgecolor="black", label="Process")

# Create range of x values (bell curve)
x = np.linspace(df_values.min(), df_values.max())

# Plot a bell curve using data's mean and std
plt.plot(x, stats.norm.pdf(x, mean, std), color='red', label="Normal Distribution")

# Add titles, labels, legend and grid
plt.title("Bell Curve of Process Data")
plt.xlabel("Successful Process Deadline")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("bell_curve.png")
plt.show()
