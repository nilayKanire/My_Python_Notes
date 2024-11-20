'''
How Import Works in Python
'''

import sklearn as sk
print(sk.__version__)               # Here we named sklearn as sk and then we finding its version by sk.__version__

# import sys
# print(sys.path)       # sys.path is a path which gives us a path of a various types of modules.

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)

import file2
print(file2.a)        # Normally use this file2.a method as a beginner.
# OR
# from file2 import a
# print(a)
file2.printjoke("this is me")
