class Employee: 
    def __init__(s,n,sal):
        s.n=n;
        s.sal=sal
    def show(s):
        print(s.n, s.sal)
class Manager(Employee):
    pass
Manager("ravi",5000).show()



#Store name & salary in constructor
#Create a show() method to display details
