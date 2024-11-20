'''
Abstract Base Class & @abstractmethod
'''
# abc module hota hai python me,aur ABCMeta class hamari ye hoti hai ki hum kisi bhi class ko ABCMeta class se inherit karenge tab vo class apne baccho ko , matlab apne child classes ko aadesh de sakti hai , ki aapko kuch methods ko implement karna hii karna hai.
from abc import ABCMeta, abstractmethod                   # abstractmethod jo hai vo ek decorator hota hai, aur abc python me ka ek module hai.

class Shape(metaclass=ABCMeta):
    @abstractmethod                                    # yaha abstractmethod isliye likha q ki sabko vahi define karna padega jo useme likha  hai.
    def printarea(self):                              # Agar hum Shape class se  Inherit kar rahe ho toh ye zaroori hai ki aap print area ko apne  andar define kare, ye rectangle class se bola jaa rha hai. Rectangle class ko shape wali class ye aadesh deti hai ki aapko print area waale function ko impliment  karna hai.
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# tryobj = Shape()                                                   # Abstract base class k object nahi banaya ja sakte.