#Inheritance: one class can take properties and behaviour from another


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)  # can also use super().__init__(name, salary)
        self.department = department
        self.team_size = 0

    def show_team_size(self):
        print(f"Department: {self.department}")
        print(f"{self.name} manages a team of {self.team_size} members")
        print("------------------------------------")

class Developer(Manager):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary, department = "Software")
        self.programming_language = programming_language


    def show_details(self):
        super().show_details()
        print(f"Progarmming Languages: {self.programming_language}")


m1 = Manager("Alice", 80000, "HR")
m1.team_size = 5

print("Manager Details:")
m1.show_details()
m1.show_team_size()

d = Developer("Tom", 50000, "Python")
d.show_details()
'''
multilevel inheritance: a child class becomes parent to another child class
hierarchial inheritance:  multiple child classes inherit from a single parent class
single inheritance: one child class inherits from one parent class
multiple inheritance: one child class inherits from more than one parent class
'''
'''
class Mother:
    def mother(self):
        print("mothers method")
class Father:
    def father(self):
        print("fathers method")
class Child(Mother, Father):
    pass
c = Child()
c.mother()
c.father()
'''

