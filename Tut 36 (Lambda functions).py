'''
ANonymous/ Lambda Functions In Python
'''
# Lambda functions or anonymous functions

def add(a, b):
    return a+b

minus = lambda x, y: x-y              # Lambda is a one liner function
#        ^^^
#        |||              <<-- This lambda single line is == below def & return line. 
#        vvv
# def minus(x, y):
#     return x-y

print(minus(9, 4))

def a_first(a):
    return a[1]

a = [[1, 14 ], [5, 6], [8, 23], [2,7]]      # Key is an Argument which takes Function as a Input.
#a.sort(key= a_first  )                  # This 'a_first' funtion is returning us a whatever going inside it , returning us a first index.
a.sort(key=lambda x:x[1])             # Sort function k property hoti hai ki vo key= as function ka naam leta hai.
print(a)