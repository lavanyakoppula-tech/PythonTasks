def gen(n):
    for i in range(1,n+1):
        yield(i)

for x in gen(10):
    print(x)





#Use yield to create a generator function
#It produces values one by one (1 to N) instead of all at once
#Loop (for x in gen(n)) prints each value step-by-step
