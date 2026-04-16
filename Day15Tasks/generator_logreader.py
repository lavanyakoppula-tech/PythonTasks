# Generator function to read file line by line
def read_logs(file_name):
    with open(file_name, 'r') as file:   # FIXED HERE
        for line in file:
            yield line.strip()
 
 
# Dictionary to store error counts
error_count = {}
 
# Using the generator
for log in read_logs("log.txt"):
    # Condition to filter errors
    if "ERROR" in log:
        # Count occurrences
        if log in error_count:
            error_count[log] += 1
        else:
            error_count[log] = 1
 
 
# Print results
print("Error occurrences:")
for error, count in error_count.items():
    print(error, "->", count)
