# Dictionary is nothing but key value pairs
d1 = {}       # d1 = []  , d1 = ()
print(type(d1))
d2 = {"Nilay":"Burger",           # " key "  : " items ",
      "Rohan":"Fish",
      "skillf": "Roti",
      "Shubham":{"B":"maggie", "L":"roti","D":"chicken"}}   #<<-- This is showing that we can make a dictionary inside a dicationary.
print(d2)
print(d2["Nilay"])
#print(d2["Shubam"]["B"])

d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2)

"""
|||some function of dictionary
VVV
"""
print(d2.copy())
d3 = d2          # wrong function means they are not function # d3 & d2 are pointers which points their dictionary.
print(d3)
print(d2.get("Nilay"))

d2.update({"Leena":"Toffee"})
print(d2)

print(d2.keys())
print(d2.items())
"""
Search for dictionary function Python on google
"""

words= ["Apple", "Banana", "Car", "Dolphin" ]
for word in words:
 #This loop is fetching word from the list
      print ("The following lines will print each letters of "+word)
for letter in word:

# This loop is fetching letter for the word
      print(letter)
      print("")