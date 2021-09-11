# Basic Principles of OOP

# There are four basic principles of OOP. They are encapsulation, abstraction, inheritance, and polymorphism.

# Encapsulation refers to bundling data with the methods operating with it while restricting direct access
# to some components.

# Link of Special(Magic / Dunder) Method Doc. : https://docs.python.org/3/reference/datamodel.html#special-method-names
# Creating Classes and How it works
import datetime


class Example:
    pass  # if you want to skip for now you can write 'pass' under class


class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    # __init__ method run every time we run Employee class. (__init__ named as constructor)
    def __init__(self, name, last, pay):  # self is the instance we can rename it but better the use it as self
        self.name = name  # instance variables
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    @property
    def email(self):
        return "{}.{}@company.com".format(self.name, self.last)

    def fullname(self):
        return "{} {}".format(self.name, self.last)

    # I did name_surname method to not change fullname method
    @property
    def name_surname(self):
        return "{} {}".format(self.name, self.last)

    @name_surname.setter
    def name_surname(self, name):
        name, last = name.split(" ")
        self.name = name
        self.last = last

    @name_surname.deleter
    def name_surname(self):
        print("Deleted Name!")
        self.name = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # With This Decorator we make class named set_raise_amt
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_Workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # __repr__ method uses for debugging, logging and things like that. It will seems other developers.
    # At least we have __repr__ method in out code.
    def __repr__(self):
        return f"Employee({self.name}, {self.last}, {self.pay})"

    # __str__ method more readable presentation of an object. It meant to display to the user.
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # __add__ method helps us to make arithmetic operation with objects
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):  # Developer class inherit Employee class
    raise_amount = 1.10  # we can override a data and it's not influence anything in Employee class

    def __init__(self, name, last, pay, prog_lang):
        # with super().__init__() we can allow Employee __init__ method to handle name,last and pay.
        # So we can not repeat ourself.
        super().__init__(name, last, pay)
        # Employee.__init__(self, name, last, pay)  # is same with super. if we use multiple inheritance,
        # we can use this otherwise super can be more maintainable.

        self.prog_lang = prog_lang


class Manager(Employee):
    # Why we did not create employees as list ? Because Collection types should not define as default.
    def __init__(self, name, last, pay, employees=None):
        super().__init__(name, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# we created 2 Employee
emp_1 = Employee('Ahmet', 'Budak', 60000)  # emp_1 is an instance
emp_2 = Employee('Jim', 'Care', 50000)

# print(emp_1.fullname())  # we write self in func. because fullname method automatically passes the Employee Object
# print(Employee.fullname(emp_1))  # doing the same thing with above
# print(emp_1.pay)

# emp_1.raise_amount = 1.05  # if we try to change raise amount value, it will create new variable inside emp_1
# print(emp_1.__dict__)
# Employee.raise_amount = 1.05  # we can change the value of raise_amount like that

# print(Employee.num_of_employees) # counts employees created with Employee class

# Employee.set_raise_amt(1.05)  # with @classmethod we raise amount
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# we created string values
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-70000'

# Called from_String class to return employees are string format
new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email, "\nNum of Employees: ", Employee.num_of_employees)

# defining @staticmethod for working date static methods don't passes classes or instances
my_date = datetime.date(2016, 7, 11)
# print(Employee.is_Workday(my_date))  #  checking whether it's my workday nor not

# print(help(Developer))  # checking the Developer class

dev_1 = Developer('Ahmet', 'Budak', 60000, 'Python')
dev_2 = Developer('Jim', 'Care', 50000, 'C')

# print(dev_1.email)
# print(dev_1.prog_lang)

mng_1 = Manager('Sue', 'Smith', 100000, [dev_1])  # we created manager with Manager class
# print(mng_1.print_employee())
mng_1.add_employee(dev_2)  # we added employee to mng_1 to supervise
# print(mng_1.print_employee())
mng_1.remove_employee(dev_1)  # we removed employee to mng_1
# print(mng_1.print_employee())

# isinstance() and issubclass() uses to check inheritance between classes
# print(isinstance(mng_1, Manager))
# print(isinstance(mng_1, Employee))
# print(isinstance(mng_1, Developer))

# print(issubclass(Developer, Employee))  # Is Developer class sub-class of Employee class? Yes
# print(issubclass(Employee, Developer))  # Is Employee class sub-class of Developer class? No
# print(issubclass(Developer, Manager))  # Is Developer class sub-class of Manager class? No
# print(issubclass(Manager, Developer))  # Is Manger class sub-class of Developer class? No

# SPECIAL METHODS
# These are also called magic or dunder methods. These methods allow us to emulate
# built-in types or implement operator overloading.

# double under score is called dunder(like __init__ methods).


print(emp_1.__repr__())  # for developers to see. Should have in code.
print(emp_1.__str__())  # for user to see.


print(emp_1 + emp_2)  # with the help of __add__ method we can sum 2 objects pay value
# print(emp_1.__len__())


# PROPERTY DECORATORS
# The property decorator allows us to define Class methods that we can access like attributes.
# This allows us to implement getters, setters, and deleters.

emp_1.name = 'Mehmet'  # when we changed name, name and fullname method automatically changed but email didn't.
# For this, we use property decorators: getters, setters, deleters

# if we create email method() like fullname() method, people uses our code have to change the code every time
# we makes changes like emp_1.email to emp_1.email(). To get rid of the method we use @property above def email() method

print(emp_1.name)
print(emp_1.email)  # with the help of @property we can use email method like attribute.
print(emp_1.fullname())

emp_1.name_surname = "Marcus Denial"  # give value to method like attribute to the help of @property

del emp_1.name_surname  # when we run del, deleter property run.
