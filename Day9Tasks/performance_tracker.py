import time   

# Decorator function
def time_tracker(func):
    def wrapper():
        start = time.time()      # start time
        func()                   # call original function
        end = time.time()        # end time
        print("Execution Time:", end - start, "seconds")
    return wrapper


# Function to test performance
@time_tracker
def task():
    for i in range(10000):
        pass


# Main function
def main():
    task()


# Entry point
if __name__ == "__main__":
    main()
