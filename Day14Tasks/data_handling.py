import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
S=pd.Series(arr)
print(S)
mean_value = S.mean()

S = S.fillna(mean_value)

print("Mean value:", mean_value)
print("Updated Series:")
print(S)
