class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str, salary: float):
        # Using super() to call parent class constructor
        super().__init__(name, age)
        # Encapsulation: Private variables
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter and Setter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id: str):
        self.__employee_id = employee_id

    # Getter and Setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary: float):
        self.__salary = salary

    # Overriding display method
    def display(self):
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ${self.get_salary():.1f}")


class Manager(Employee):
    def __init__(self, name: str, age: int, employee_id: str, salary: float, department: str):
        # Using super() to call Employee constructor
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Overriding display method
    def display(self):
        super().display()
        print(f"Department: {self.department}")


def main():
    # Storage for created entities
    created_person = None
    created_employee = None
    created_manager = None

    while True:
        print("--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            created_person = Person(name, age)
            print(f"\nPerson created with name: {created_person.name} and age: {created_person.age}.\n")

        elif choice == "2":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            created_employee = Employee(name, age, emp_id, salary)
            print(
                f"\nEmployee created with name: {created_employee.name}, age: {created_employee.age}, "
                f"ID: {created_employee.get_employee_id()}, and salary: ${created_employee.get_salary():.1f}.\n"
            )

        elif choice == "3":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            created_manager = Manager(name, age, emp_id, salary, dept)
            print(
                f"\nManager created with name: {created_manager.name}, age: {created_manager.age}, "
                f"ID: {created_manager.get_employee_id()}, salary: ${created_manager.get_salary():.1f}, "
                f"and department: {created_manager.department}.\n"
            )

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            detail_choice = input("Enter your choice: ")

            print()
            if detail_choice == "1":
                if created_person:
                    print("Person Details:")
                    created_person.display()
                else:
                    print("No Person object created yet.")
            elif detail_choice == "2":
                if created_employee:
                    if issubclass(Employee, Person):
                        print("Employee Details:")
                        created_employee.display()
                else:
                    print("No Employee object created yet.")
            elif detail_choice == "3":
                if created_manager:
                    if issubclass(Manager, Employee):
                        print("Manager Details:")
                        created_manager.display()
                else:
                    print("No Manager object created yet.")
            else:
                print("Invalid choice.")
            print()

        elif choice == "5":
            print("\nExiting the system. All resources have been freed.\n")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again.\n")

        print("--- Choose another operation ---\n")


if __name__ == "__main__":
    main()