'''
Super() & Overriding() IN Classes
'''

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar2 = "I am in class B"
                                                                         # super class k constructor ko call karne k liye hum super ka use karte hai.
    def __init__(self):                                                  # class A ka constructor init wala override ho gaya hai , class B ka constructor k karan.
        #super().__init__()                                               # isiliye humne class b k constructor me   super().__init__() ko use kiya q ki hume jo var chahiye tha vo class A me tha jo class B k constructor k karan override ho gaya tha.
        self.var1 = "I am inside class B's Constructor"                 # yaha super() matlab apan ne iss class ko super constructor bana dia hai.
        self.classvar1 = "Instance var in class B"
        super().__init__()                                             # Agar apan ye super wali line class B k constructor variable k niche likhenge toh phir  class A k var run karenge .q ki super aur constructor ko bad me call kiya hai aur phir class B k var ka chalna na chalna k barabar ho sakta hai.
        print(super().classvar1)

a = A()
b = B()

print(b.classvar1)
print(b.special, b.var1, b.classvar1)