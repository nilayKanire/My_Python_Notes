'''
Join Function IN Python
'''

lis = ["John", "Cena", "Randy", "Orton",
       "Sheamus", "Khali", "Jinder Mahal"]

# for item in lis:
#     print(item, "and", end=" ")      #<-- This code is a normal way to add ' and ' after the end of each item

a = " and ".join(lis)                    #<<-- here we use and funtion to join the 'and' at the end of each item form the list.
print(a, "other wwe superstars")         # we can add/join anything after item in list .ex- a = " , ".join(lis)