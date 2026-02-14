# Composite Design Pattern

# Multiple classes that inherit from the same interface or parent class
# One of those can consist of many of the others
# imagine a regions can consist of many sub-regions
# and those sub-regions can also consist of other sub-regions

# Or a boxes in the box

from abc import ABCMeta, abstractmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in Child Class """
        pass

    @abstractmethod
    def update_department(self):
        """ Implement in Child Class """
        pass

# Leaf
class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def update_department(self):
        print("Updating Accounting...")

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

# Leaf
class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def update_department(self):
        print("Updating Development...")

    def print_department(self):
        print(f"Development Department: {self.employees}")

# Composite
class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []

    def update_department(self):
        print("Updating Parent Department and all sub-departments...")
        for department in self.sub_departments:
            department.update_department()

    def add(self, department):
        self.sub_departments.append(department)
        self.employees += department.employees

    def print_department(self):
        print("===== Parent Department =====")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for department in self.sub_departments:
            department.print_department()
        print(f"Total number of employees: {self.employees}")

department1 = Accounting(200)
department2 = Development(170)

parent_department = ParentDepartment(30)
parent_department.add(department1)
parent_department.add(department2)

parent_department.print_department()