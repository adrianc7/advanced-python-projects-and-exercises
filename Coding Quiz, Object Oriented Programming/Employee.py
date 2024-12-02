class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def salary_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return self.salary

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: ${self.salary:.2f}"

# Initialize employee John with a salary of 5000
john = Employee("John", 5000)

# Apply a 10% raise
new_salary = john.salary_raise(10)

# Print the updated salary
print(john.display_info())

