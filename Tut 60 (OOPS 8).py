'''
Single Inheritance
'''

class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)          # agar iss tarah ek function  banana ho jo na self ko as a  argument le na cls ko as a argument le , Kare kya sirf khud apne aap me kaam kare jisme hamara koi bahar class k koi function hota.
        # return

#----------------------------------------Single Inheritance-----------------------------------------

class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages




    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.languages}"


harry = Employee("harry", 455, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555 , "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["c++"])
print(karan.printprog())
print(karan.no_of_holiday)

