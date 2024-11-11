

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee: {self.name} (ID: {self.employee_id}) - Salary: ${self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to ${self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name}.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name}: ${total_salary}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for employee in self.employees:
            employee.display_details()


# Interactive code for managing employees and departments
def interactive_employee_management():
    department = Department("Engineering")

    while True:
        print("\nEmployee Management System")
        print("1. Add employee")
        print("2. Update employee salary")
        print("3. Display all employees")
        print("4. Calculate total salary expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == '2':
            employee_name = input("Enter employee's name: ")
            new_salary = float(input("Enter new salary: "))
            employee = next((e for e in department.employees if e.name == employee_name), None)
            if employee:
                employee.update_salary(new_salary)
            else:
                print(f"Employee {employee_name} not found.")

        elif choice == '3':
            department.display_all_employees()

        elif choice == '4':
            department.calculate_total_salary()

        elif choice == '5':
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

()
