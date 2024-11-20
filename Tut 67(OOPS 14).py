'''
Operator Overloading & Dunder Methods
'''

'''
Search - Mapping Operators to Functions for python 
(To know more function related to this topic)
'''
class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):                  # __add__ ye ek special method hai aur hum ise Dunder add kahte hai. Aur ye hume madat kar raha hai Opertaor Overloading karne me. par zaroori nahi hai Hamesha ki vo operator ko  overloading kare.
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        #return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
        return f"Employee('{self.name}', '{self.salary}', '{self.role}' )"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# under score-under score(__ - __) se start hone wale aur end hone wale method jo hote hai use kahte hai ' init ' , aur iskko kahte hai Dunder init.
'''
Dunder init ek special method hota hai, kyuki ye ek constructor hai , isko jo bhi argument denge vo run ho jayega , vo function pura run ho jayega jab bhi object ban raha hoga.
'''

emp1 = Employee("Harry", 345, "Programmer")         # ctrl + d  - Replicate ho jati hai line puri.
emp2 = Employee("Rohan", 85, "Cleaner")

print(emp1 + emp2)                               #kisi bhi 2 object ko hum jodte hai, toh vo Dunder add method ko jo insight jo hai behind the scenes run karta hai.
print(emp1 / emp2)
print(emp1)                      # agar hum emp1 ko print karna chaah rahe hai toh phir vo str wale method sabse pahle run karna prefer karega.
                                 # agar str maujud nahi hai toh phir print karne par bhi repr dikhaye ga aur str karne par bhi repr dikhayega.
print(str(emp1))
print(repr(emp1))