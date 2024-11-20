'''
Python 'is' vs '==': What's The Difference?
'''

# ==  -  value equality  -  Two objects have the same value
# is  -  reference equality  -  Two references refer to the same object

# Task
from time import time
init = time()
a = [6,4, "34"]
b = [6,4, "34"]

print(a is b)

print(a == b)
print("overall time :  ", time() - init)