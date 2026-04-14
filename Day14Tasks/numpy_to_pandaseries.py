import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40])

S = pd.Series(arr, index=["A", "B", "C", "D"])

print(S)
