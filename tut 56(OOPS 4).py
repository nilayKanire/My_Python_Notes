'''
Class Methods In Python
'''
class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod                                   # iss class method me hume 'self' nahi milta , kyuki isme sirf apan class k saath hii khilwad kar sakte hai.
    def change_leaves(cls, newleaves):              # cls hai vo class jiska instance hai yaha 'harry' vala object, harry.no_of_leaves.  In this harry is instance.
        cls.no_of_leaves = newleaves

# class method sirf class k instance variable ko excess kar payega, Aur hum isko kisi instance se ya phir kisi bhi class se bhi excess kar sakte hai.
# class method me 'instance' self ko input na lekar 'class' ko input leta hai , aur jo bhi argument humne class me likhe hai unko bhi input le isliye hum class method ka use karte hai.

harry = Employee("harry", 455, "Instructor")
rohan = Employee("Rohan", 455, "Student")

harry.change_leaves(34)

print(harry.no_of_leaves)

