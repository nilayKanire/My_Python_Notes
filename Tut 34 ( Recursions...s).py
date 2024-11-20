'''
Recursions: Recursive Vs Iterative Approach
'''

def print2(str1):
    print(str1)
    print("This is " + str1)

print2("harry")



def factorial_iterative(n):          # here this factorial is maths vala factorial
    """
     # This doc string |||
                       VVV
    :param n: Integer
    :return: n * n-1 * n-2 * n-3.....1
    """
    fac = 1
    for i in range(n):            # this iteratin of 'i' starts from 0 and end at a no. less than 'n'
        fac = fac * (i+1)
    return fac


number = int(input("Enter the number: \n " ))
print("Factorial using iteratve Method",factorial_iterative(number))                       # This is finding factorial using iterative function approach

# n! = n * n-1 * n-2 * n-3.....1
# n! = n * (n-1)!

def factorial_recursive(n):
    """
    :param n:
    :return:
    """

    if n ==1:
        return 1

    else:
        return  n * factorial_recursive(n-1)
# this operations are happeing in else funtion here
'''
5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * factorial_recursive(1)
5 * 4 * 3 * 2 * 1 = 120                      when this line comes to 1 factorial then this operation will directly goes up to the if funtion in return side
'''


number = int(input("Enter the number: \n"))
print("Factorial Using Recursive Method", factorial_recursive(number))


'''
Quiz - we have to write the funtion for calculating Fibonacci function          # 0 1 1 2 3 5 8 13 ...n

'''
# we have to find the nth Fibonacci function

def fibonacci(n):
    if n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("Enter the number: \n "))
print("fibonacci factorial using Recursive Method", fibonacci(number))  # This is finding factorial using iterative function approach

# Tips - For debugging dont use Recursive  method use only Iterative method
#         But for normal running programm use Recursive method only because
#         this method is not lengthy like Iterative method.