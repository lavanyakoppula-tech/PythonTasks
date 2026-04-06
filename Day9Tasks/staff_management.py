class Staff:
    def __init__(s,name): s.name = name
    def show(s): print("Name:", s.name)

class Professor(Staff):
    pass
class LabAssistant(Staff):
    pass
class Administrator(Staff):
    pass

p = Professor("Ravi")
l = LabAssistant("Anu")
a = Administrator("Kiran")

p.show()
l.show()
a.show()



#Hierarchical Inheritance = One base class, many child classes
#All child classes share common properties from parent
