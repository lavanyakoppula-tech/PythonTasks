# Define a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 95
}

# Find the student with the highest marks
top_student = max(student_marks, key=student_marks.get)
top_marks = student_marks[top_student]

# Print the result
print(f"The student with the highest marks is {top_student} with {top_marks} marks.")
