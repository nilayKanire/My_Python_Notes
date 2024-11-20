'''
Multilevel Inheritance
'''

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no. of times"

class Grandson(Son):                         # Grandson - Son ka inheritance hai ,aur Son - DAd ka inheritance .

    dance = 6                              # dance , guitar , basketball,etc jo class k andar likhe hai usse Attribute kahte hai.

    def isdance(self):                       # yaha ' O ' ka matlab ye hai ki yaha jo isdance vala method tha ab vo lagu hoga, purana wala isdance method nahi lagu hoga.
        return f"Jackson yeah!"\
               f"Yes I dance very awesomely {self.dance} no. of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())

print(harry.basketball)

'''
Quiz
'''
# electronic device
# pocket gadget
# phone