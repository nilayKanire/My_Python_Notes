'''
Public, Protected & Private Access Specifiers
'''

class Employee:
    no_of_leaves = 8
    var = 8
    _protect = 9                               # _protect ka matlab hai ki apna ye jo protected variable hai vo , sirf iss class me istemal kar sakte hai, ya phir isse banai jane wali aage koi bhi  class me istemal kar sakte hai.
    __private = 98                             #  __private vale variable ko python 'NAME MANGLING' kar deta hai . Matlab bhale hi apan ne Attribute private name diya ho par , vo private hone k karan kisi aur name se output lena padta hai.

    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

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

emp = Employee("harry", 343, "Programmer")
print(emp._protect)

print(emp._Employee__private)              # private hone k karan hume iss me, ' _Employee ' add karn pada ' __private ' k pahle. kyuki private hone k karan python me NAME MANGLING hota hai.