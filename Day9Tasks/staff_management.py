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
