import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Students": students, "Marks": marks})

# line graph
plt.subplot(2,3,1)
plt.plot(df["Marks"])
plt.title("Line Graph")

# bar chart
plt.subplot(2,3,2)
plt.bar(df["Students"], df["Marks"])
plt.title("Bar Graph")

# pie chart
pass_count = sum(df["Marks"] > 50)
fail_count = sum(df["Marks"] <= 50)
plt.subplot(2,3,3)
plt.pie([pass_count, fail_count], labels=["Pass", "Fail"])
plt.title("Pie Chart")

# histogram
plt.subplot(2,3,4)
plt.hist(df["Marks"])
plt.title("Histogram")

# scatter plot
plt.subplot(2,3,5)
plt.scatter(range(len(df)), df["Marks"])
plt.title("Scatter Plot")

# important for proper layout
plt.tight_layout()

# display all in one window
plt.show()
