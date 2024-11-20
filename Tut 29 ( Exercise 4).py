'''
Asrtologer's Stars
'''
# Pattern Printing

# Input = Integer          n- it is the number of rows
# Boolean =  0 and 1 (True or False
#
# True n=4
# *
# **
# ***
# ****
#
# False n=4
# ****
# ***
# **
# *


# row = int(input("Enter the number of rows \n"))
# inp1 = bool(input("Enter 0 or 1\n"))
#
# if inp1 == True:
#     for i in range(1, row+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# elif inp1 == False:
#     for i in range(row,0,-1):
#         for j in range(1,i+1):
#             print("*", end="")
#         print()












'''
solution
'''
#
# print("Astrologer's Stars")
#
# a = True
# b = False
# c = input('Star pattern printing\n')
#
# if c == a:
#     print('here is the pattern ,\n')
#     print('*,\n'
#           '**,\n'
#           '***, \n'
#           '****')
# else:
#     print("Here is the pattern")
#     print("**** ,\n"
#           "***, \n"
#           "**, \n"
#           "*")

from time import time
init = time()
print("How Many Row You Want To Print")
row = int(input())
print("Type 1 Or 0")
two = bool(int(input()))
# new =bool(two)
if two == True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif two ==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()

print("Time: " , time() - init )
