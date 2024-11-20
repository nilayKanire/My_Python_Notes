'''
Raise in Python + Examples
'''
from time import time
'''
init = time()
a = input("What is your name \n")
b = input("How much do you earn\n")

if int(b)==0:
    raise ZeroDivisionError("b i 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed \n")         # there are different types of error in python. we have to search - built in Exceptions . to explore more error.

print(f"Hello {a} \n")
print("overall time : ",time() - init)
'''
# 1000 lines taking 1 hour

# Task - Search for Built in Exceptions in python for different errors

c = input("Enter your name\n\t")

try:
    print(a)

except Exception as e:
    if c == "harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")