import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90]) 

df = pd.DataFrame({"Names": names, "Marks": marks})

plt.bar(df["Names"], df["Marks"])
plt.show()
