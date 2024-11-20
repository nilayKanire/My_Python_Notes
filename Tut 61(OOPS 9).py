'''
Multiple Inheritance
'''

class Employee:
    no_of_leaves = 8
    var = 8
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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

'''
______________________________________Multiple Inheritance____________________________________________
'''

class CoolProgrammer(Employee,Player):                         # bracket k andar sequence k order se class k name likhne hai jo humne likhe hai upar.
    var = 10
    language = "c++"
    def printlanguage(self):                             # yaha humne class me printlanguage naam ka method banaya hai.
        print(self.language)
    pass                                                 # yaha CoolProgrammer class jo hai vo  class Employee aur class Player ka inheritance hai.
# class CoolProgrammer = class Employee + class Player ko inherit kiya hai.

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", 8999, "CoolProgrammer")

# det = karan.printdetails()
# karan.printlanguage()
# print(det)

print(karan.var)                        # agar koi Attribute ya or koi bhi method apan use kara rahe ho, jo ki dono classes me hai toh phir vo sabse pahle vahi class ka input lega jo sabse pahle likhi ho.
print(shubham.var)
print(harry.var)
