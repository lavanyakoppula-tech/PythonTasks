import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
S=pd.Series(arr)
print("panda series:\n",S)
print("greater values:\n",S[S > 20])
