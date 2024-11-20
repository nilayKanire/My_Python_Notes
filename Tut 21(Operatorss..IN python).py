'''
Types of Operator In Python
'''
# Arthmetic Operator
# Assignment Operator
# Comparison Operator
# Logical Operator
# Identity Operator
# Membership Operator
# Bitwise Operators
'''
1.  Arithmetic Operator
'''
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is " , 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)          # This gives exponential - (power) i.e. here 5^3 = 125
# print("27 % 5 is ", 27%5)          # This gives Remainder afer division i.e. here 27 % 5 is 2
# print("15 // 6 is ", 5//6)         # This gives integer value after division i.e. If the value comes after div is 0.833 , Then it gives integer value 0.


'''
2.  Assignment Operators
'''
print("Assignment Operators")
x = 5
print(x)                       # += is an operator
x += 7                         # This meaning is  x = x+7
                               # we can use the other signs shown in Arthmetic Operator which available in Assignment Operator.
                               # signs like ( - , % , etc.)
print(x)

'''
3.   Comparison Operators
'''
i = 5
print( i == 5)                # == means we are comparing two things.
print( i != 5)                # != means not equalto sign.
print( i >= 5)
print( i <= 5)


'''
4.  Logical Operators
'''
a = True
b = False

print(a and b)
print(a or b)

'''
5.  Identity Operators
'''
print("Identity Operators")
a = True
b = False

print(a is b)
print(a is not b)
print(5 is 5)
print(5 is not 5)

'''
6.  Membership Operators
'''
print("Membership Operators")
list = [3, 3, 2 ,2, 39, 33, 35, 32]
print(324 in list)
print(324 not in list)
'''
7. Bitwise Operators         # This operators works with Bit mean Binary no. ( 1 & 0 ) 
'''
0 - 00

2 - 10
3 - 11

print( 0 & 3)
print( 0 | 3)