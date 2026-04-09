import numpy as np
Branch_A=np.array(
     [[10, 20],
      [30, 40]])
Branch_B=np.array(
     [[5, 15],
      [25, 35]])
combine=Branch_A+Branch_B
print("combined matrix\n",combine)
total_employees=np.sum(combine)
print("total:",total_employees)
