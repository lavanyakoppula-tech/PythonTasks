import numpy as np
import pandas as pd
arr = np.array([ 
 [100, 200], 
 [150, 250], 
 [80, 120], 
 [300, 400] 
])
print(arr)
df=pd.DataFrame(arr,columns=["Sales","Profit"])
print(df)
filtered = df[df["Sales"] > 100]

print(filtered)

print("Average Profit:\n", filtered["Profit"].mean())
