import numpy as np
import pandas as pd
import time


# Decorator to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\nExecution Time:", end - start, "seconds")
        return result
    return wrapper


# Generator to read numbers from file
def read_numbers(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()


# Main processing function
@measure_time
def process_data(file_name):
    numbers = []

    # Using generator + exception handling
    for value in read_numbers(file_name):
        try:
            num = float(value)   # convert to number
            numbers.append(num)
        except ValueError:
            print("Skipping invalid data:", value)

    # Convert to NumPy array
    arr = np.array(numbers)

    # NumPy calculations
    mean_val = np.mean(arr)
    std_val = np.std(arr)

    # Convert to Pandas DataFrame
    df = pd.DataFrame({
        "Mean": [mean_val],
        "Standard Deviation": [std_val]
    })

    return df


# Call the function
result_df = process_data("numbers.txt")

# Print results
print("\nProcessed Data:")
print(result_df)
