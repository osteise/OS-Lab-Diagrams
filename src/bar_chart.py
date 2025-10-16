import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Process without setdl": [5, 10, 5, 9, 7, 10, 10, 10, 8, 5],
    "Process with setdl": [8, 8, 10, 7, 10, 10, 10, 10, 10, 10]
}

df = pd.DataFrame(data)

# The x-position order of bars
barsOrder = range(len(df.columns))

# Bars Data
barsData = df.mean()

# width of the bars
barWidth = 0.6

# Std Bars Interval
barsInterval = df.std()

# Opacity of colours
Opacity=0.8

# Interval cap size
intervalCapsize=7

# Plot bars
plt.bar(barsOrder, barsData, color = "lightblue" , edgecolor = 'black', width = barWidth, yerr=barsInterval, capsize=7, alpha=Opacity, bottom=intervalCapsize)

#Put a tick on the x-axis undex each bar and label it with column name
plt.xticks(range(len(df.columns)), df.columns)

# Add titles, labels and grid
plt.title('Average Successful Process with Standard Deviation')
plt.xlabel('Process Type')
plt.ylabel('Success Score')
plt.grid(alpha=0.3)

plt.savefig("STDBarChart.png")
plt.show()