# Decorator to add bonus
def add_bonus(func):
    def wrapper(self):
        bonus_amount = 1000              # fixed bonus
        self.salary += bonus_amount      # modify salary
        func(self)                       # call original function
    return wrapper


# Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self):
        print("Employee:", self.name)
        print("Salary after bonus:", self.salary)


# Main function
def main():
    emp = Employee("John", 5000)
    emp.display_salary()


# Entry point
if __name__ == "__main__":
    main()
