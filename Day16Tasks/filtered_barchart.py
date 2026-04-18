import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]
df = pd.DataFrame({"Names": names, "Marks": marks})
filtered = df[df["Marks"] > 50]

plt.bar(filtered["Names"], filtered["Marks"])
plt.show()
