'''
Instance & Class Variables
'''

class Employee:
    no_of_leaves = 8            #ye no_of_leaves sirf harry ya rohan ki nahi . par dono ki milke hai dono , share karre hai ye no of leaves iss class ki hai.
    pass

harry = Employee()              # harry and rohan are derived from the class
rohan = Employee()

harry.name = "Harry"                 # --------
harry.salary =  445                  #          -----
harry.role = "Instructor"            #               ----
                                               #         --- This all are variables of the instances .                                       objects in class.
rohan.name = "Rohan"                 #               -----
rohan.salary = 7434                  #           -----
rohan.role  = "Student"              # ---------

print(rohan.no_of_leaves)           # no_of_leaves ka record ye class rakh rahi hai , ye no. of leaves sabke liye same hai.
# here rohan & harry are instance.

print(Employee.no_of_leaves)         # here Employee is class. we are accesssing the variable (no_of_leaves) with class.
print(Employee.__dict__)
Employee.no_of_leaves = 9
rohan.no_of_leaves = 9               # this rohan statement will not cahnge the no. of leaves coz it will create instance for rohan , means we cant change the class variable with Instance or with instance variable.
print(Employee.no_of_leaves)

print(rohan.__dict__)               # __dict__ is not an function but attribute which return  dictionary to us.
print(Employee.__dict__)