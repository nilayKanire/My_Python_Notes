'''
Setters & Property Decorators In Python
'''

class Employee:
    def __init__(self, fname, lname ):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"               # yaha email Attribute hai. isliye humne print me hindustani_supporter.email likha hai , email k bad () ye nahi lagaya hai.

    def explain(self):                                           # yaha pe function likha hai, jo ki explain karega employee ko.
        return f"This employee is {self.fname} {self.lname}"       #isss problem ko solve karta hai 'Setter'. isliye humne email as function define kiya phir usse hindustani_supporter.email ke bad parenthesis () lagaya q ki ab hum us email ko as a function use karre hai.

    @property                       # ye @property ek decorator hai. jab humne ye property decorator laga diya apne is email function me toh hume usse as a function [ matlab email likne k baad () ye lagane ki jaroorat nahi hai ] run karne k koi jarrorat nahi hai.
    def email(self):                                         #yaha email function hai.
        return f"{self.fname}.{self.lname}@codewithharry.com"


hindustani_supporter = Employee("Hindustani", "Supporter")                        # ye object banaye hai hindustani_supporter & nikhil.....
nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)                  # Jab hum yaha email as a function liya tab parenthesis () use karna important hai email k bad.

#-------------------------Quiz-------------------------------------
'''
Batana hai ki agar hum niche ki step likhenge toh hindustani_supporter ka first name change ho kar US_supporter hoga ya nahi ?
'''

# hindustani_supporter.fname = "US"
#
# print(hindustani_supporter.email)
'''
Ans - First name change nahi hoga .
Reason - Run time me jab object ko  banaya tha yaniki object creation k time par maine hindustani supporter likha tha aur tab init constructor run hua tha aur tab usne email ko initalize kar diya tha.
          isss problem ko solve karta hai 'Setter'. isliye humne email as function define kiya phir usse hindustani_supporter.email ke bad parenthesis () lagaya q ki ab hum us email ko as a function use karre hai.
'''

#--------------------------------   Setter -----------------------------------------------

class Employee:
    def __init__(self, fname, lname ):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"               # yaha email Attribute hai. isliye humne print me hindustani_supporter.email likha hai , email k bad () ye nahi lagaya hai.

    def explain(self):                                                    # yaha pe function likha hai, jo ki explain karega employee ko.
        return f"This employee is {self.fname} {self.lname}"             #isss problem ko solve karta hai 'Setter'. isliye humne email as function define kiya phir usse hindustani_supporter.email ke bad parenthesis () lagaya q ki ab hum us email ko as a function use karre hai.

    @property                                                               # ye @property ek decorator hai. jab humne ye property decorator laga diya apne is email function me toh hume usse as a function [ matlab email likne k baad () ye lagane ki jaroorat nahi hai ] run karne k koi jarrorat nahi hai.
    def email(self):                                                      #yaha email function hai.
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting now.....")
        names = string.split("@")
        self.fname = string.split(".")[0]
        self.lname = string.split(".")[1]

    @email.deleter
    def email(self):                     #here we created email deleter using decorator becoz we cant delete function bye writing' del and name of function '
        self.fname = None
        self.lname = None



hindustani_supporter = Employee("Hindustani", "Supporter")                        # ye object banaye hai hindustani_supporter & nikhil.....
nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)                                                        # Jab hum yaha email as a function liya tab parenthesis () use karna important hai email k bad.

hindustani_supporter.email = "this.that@codewithharry.com"    # XXXXXXXXX - wrong attribute
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)
print(hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)