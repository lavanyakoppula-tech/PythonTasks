import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

print("employees:",employees)

# Shallow copy
shallow = copy.copy(employees)
shallow[0][1] = "Z"

print("shallow_copy:",shallow)

# Deep copy fix
deep = copy.deepcopy(employees)
employees[1][1] = "Y"

print("deep copy:",deep)


#Shallow copy shares inner lists
#deep copy creates full independent copy.
