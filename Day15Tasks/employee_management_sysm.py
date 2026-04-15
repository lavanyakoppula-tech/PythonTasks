class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
#store employees in a dict

employees = {}  

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Employee
    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")

        try:
            salary = float(input("Enter Salary: "))  # Exception handling
            emp = Employee(emp_id, name, salary)
            employees[emp_id] = emp
            print("Employee added successfully!")

        except ValueError:
            print("Invalid salary! Please enter a number.")

    # Display Employees
    elif choice == '2':
        if not employees:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for emp in employees.values():   # Loop
                print(emp.display())

    # Save to File
    elif choice == '3':
        try:
            with open("employees.txt", "w") as file:
                for emp in employees.values():
                    file.write(emp.display() + "\n")

            print("Data saved to file successfully!")

        except IOError:
            print("Error writing to file.")

    # Exit
    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
