import numpy as np

#Generate random numbers
nums = np.random.randint(1, 100, 10)

#filter values divisible by 5
filter_nums = nums[nums % 5 == 0]

#Sort the filtered values
sort_nums = np.sort(filter_nums)

# Output results
print("Random Numbers:", nums)
print("Numbers divisible by 5:", filter_nums)
print("Sorted Result:", sort_nums)
