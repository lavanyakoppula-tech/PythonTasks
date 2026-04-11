import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Deep copy
copied_classes = copy.deepcopy(classes)

# Modify original data
classes[0][1][0] = 99

print(classes)
#The original list is modified (30 → 99)
#The deep copied list remains unchangedprint(copied_classes)
#Why it is required:it contains contains nested lists and also create completely independent copies of all inner objects
#so changes in the original do not affect the copied data.
