'''
Creating our First Class in Python
'''
from time import time

init = time()

class Student:
    pass

harry = Student()                      # student wala ye jo hai vo object hai ,aur student object k do instance banaye hai yaha.
nilay = Student()   # 1st instance is harry & 2nd instance is nilay . Dono student class se derive karne wale instance the.




harry.name = "Harry"                 # here std , section jo instance variable the unko initialse kia kuch values se aur uske baad unhe print kia.
harry.std = 12
harry.section = "A"

nilay.std = 7
nilay.subjects = ["Electronics", "Computer Science"]

print(harry, nilay)
print(harry.section,",", nilay.subjects)

print("Overall time to execute :",time() - init )