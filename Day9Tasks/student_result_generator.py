class Result:
    def calc(s,a,b,c=None):
        if c is None:
            print("Total (2 subjects):", a+b)
        else:
            print("Total (3 subjects):", a+b+c)

r = Result()
r.calc(50,60)
r.calc(50,60,70)
