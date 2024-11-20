'''
Diamond Shape Problem In Multiple Inheritance
'''

# Diamond Shape Problem - ye ek problem hoti hai, matlab jo ek confusion jo create ho jata hai ki konsi class konse method ko istemal kare.

# Java doesn't allow Multiple inheritance ,but Python & c++ allow Multiple Inheritance.

class A:
    def meth(self):
        print("This is a method from class A")

class B(A):
    def meth(self):
        print("This is a method from class B")

class C(A):
    def meth(self):
        print("This is a method from class C")

class D(B, C):
    def meth(self):
        print("This is a method from class D")

a = A()
b = B()
c = C()
d = D()

d.meth()
c.meth()

# Normally Multiple Inheritance use nahi karte programming language me kyuki wo confusion paida karti hai , isliye Single Inheritance aur Multilevel Inheritance use karte hai normally.
