'''
Class Methods AS Alternative Constructors
'''

class Employee:
    no_of_leaves = 8
    def __init__(self, aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # @classmethod                                   # iss class method me hume 'self' nahi milta , kyuki isme sirf apan class k saath hii khilwad kar sakte hai.
    # def change_leaves(cls, newleaves):              # cls hai vo class jiska instance hai yaha 'harry' vala object, harry.no_of_leaves.  In this harry is instance.
    #     cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):                        #from_dash      jaise          from/slash     bhi likh sakte hai.
        # params = string.split("-")                   # yaha params = list banja rahi hai string se. Toh matlab param = ek list ho gayi.
        # print(params)
        # return cls(params[0], params[1], params[2])
        '''
             ^^^^
             ||||  --------------this below one line is equal to above 3 lines. This below line is one liner code for above 3 lines.
             vvvv
        '''
        return cls(*string.split("-"))                      # list me agar * lagadiya matlab as an argument pass ho jayege tino.


# class method sirf class k instance variable ko excess kar payega, Aur hum isko kisi instance se ya phir kisi bhi class se bhi excess kar sakte hai.
# class method me 'instance' self ko input na lekar 'class' ko input leta hai , aur jo bhi argument humne class me likhe hai unko bhi input le isliye hum class method ka use karte hai.
harry = Employee("harry", 455, "Instructor")
rohan = Employee("Rohan", 455, "Student")
#-------------------Alternative Constructors--------------------------------------
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
print(karan.salary)