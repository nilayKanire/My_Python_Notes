'''
Static Methods In Python
'''

class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod                                   # iss class method me hume 'self' nahi milta , kyuki isme sirf apan class k saath hii khilwad kar sakte hai.
    def change_leaves(cls, newleaves):             # cls hai vo class jiska instance hai yaha 'harry' vala object, harry.no_of_leaves.  In this harry is instance.
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):                        #from_dash      jaise          from/slash     bhi likh sakte hai.
        return cls(*string.split("-"))                      # list me agar * lagadiya matlab as an argument pass ho jayege tino.

    @staticmethod
    def printgood(string):
        print("This is good " + string)          # agar iss tarah ek function  banana ho jo na self ko as a  argument le na cls ko as a argument le , Kare kya sirf khud apne aap me kaam kare jisme hamara koi bahar class k koi function hota.
        # return


harry = Employee("harry", 455, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

# print(karan.no_of_leaves)
print(karan.printgood("Harry"))

Employee.printgood("Rohan")