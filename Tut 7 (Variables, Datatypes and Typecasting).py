'''
Type Casting
    Conversion of one data type to another is called type-casting

There are two types -  i) implicit Type Conversion
                      ii) explicit Type Conversion
'''

var1 = "hello world "       #str()
var2 = 4                    #int()
var3 = 36.7                 #float()
var4 = "Nilay"
var5 = "54 "
var6 = "32"

print(type(var1),type(var2))
print(type(var3))

print(var1 , var2)

print(var2 + var3)

print( int(var5) + int(var6))        #Typecasting

print(10 * "Hello world ")
print(10 * "Hello world \n" )

print( 100 * str(int(var5) + int(var6)))       #Typecasting in str

"""
How to take input from user |||
                            VVV
"""
#print("Enter your number")
#inpnum = input()                      #inpum is string(str)

#print("You entered ", inpum)
#print("You entered ", int(inpnum) + 10)
"""
Quiz

print("Enter first number")
n1 = input()
print("enter second number")
n2  = input()
print("sum of these numbers  is ",int(n1) + int(n2))
"""