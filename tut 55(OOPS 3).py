'''
self & __init__() (Constructors) in Python
'''
#             _______________________self_______________________________________

class Employee:
    no_of_leaves = 8

    def printdetails(self):                                # here print details is a function which can be used like, harry.printdetails(self) then it will provides harrry details.
         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}."
                                                            # after writing   printdetails      self comes automatically .

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(rohan.printdetails())

# ---------------------------------Constructors-----------------------------------------------

# Employee() function k andar argument dene k tarike  ko constructor kahte hai. means is () k andar likhna hai.
class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



harry = Employee("harry", 455, "Instructor")            # ye sab Employee() k andar k argument init ko ja rahe hai, matlab init ko hii jate hai .
rohan = Employee("Rohan", 455, "Student")

print(harry.salary)






