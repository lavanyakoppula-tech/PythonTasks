# Q1: Student Marks Management

subjects = ("Math", "Science", "English")   # tuple
students = set()                            # set
marks_dict = {}                             # dictionary

# Recursive function to calculate total
def total_marks(marks_list):
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + total_marks(marks_list[1:])

# Add student
def add_student():
    try:
        name = input("Enter student name: ")
        students.add(name)

        marks = []
        for sub in subjects:
            m = int(input(f"Enter marks for {sub}: "))
            marks.append(m)

        marks_dict[name] = marks

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

# Display students
def display_students():
    for name, marks in marks_dict.items():
        print(name, ":", marks)

# Calculate average
def calculate_average():
    try:
        name = input("Enter student name: ")

        if name not in marks_dict:
            raise NameError

        marks = marks_dict[name]
        total = total_marks(marks)
        avg = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", avg)

    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")

# Menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
