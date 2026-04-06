# Generator function
def even_generator():
    num = 2
    while True:
        yield num       # return current even number
        num += 2        # move to next even number


# Main function
def main():
    n = int(input("Enter how many even numbers you want: "))
    
    gen = even_generator()   # create generator object
    
    for _ in range(n):
        print(next(gen))     # get next even number


# Entry point
if __name__ == "__main__":
    main()
