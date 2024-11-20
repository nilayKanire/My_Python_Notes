"""
How to create Faulty Caulculator
"""
#Design a calculator which will correctly solve all the problems except
#the following ones:
#4 * 3 = 555, 56+9 = 77, 56/6 = 44
#Your program should take operator and the two numbers as input from the user
#and then return the result

print("Enter the two numbers on which you want to perform calulation")
inp1 = int(input("The first no. is\n"))

print("Now Choose the operator \n")
operator = str(input())

inp2 = int(input("The second no. is\n"))


if operator == "+":
    if inp1 == 56 and inp2 == 9:
        print(77)
    else:
        print(inp1 + inp2)

elif operator == "-":
    print(inp1 - inp2)

elif operator == "*":
    if inp1 == 4 and inp2 == 3:
        print(555)
    else:
        print(inp1 * inp2)

elif operator == "/":
    if inp1 == 56 and inp2 == 6:
        print(44)
    else:
        print(inp1 / inp2)
























#
# def calculator():
#     print("\nWellcome to Calc: This is Developed by Nilay Kanire")
#     operation = input('''
#     Please type in the math operation you would like to complete:
#     + for addition
#     - for subtraction
#     * for multiplication
#     / for division
#     ** for power
#     % for modulo
#
#     Enter Your Choice:
#     ''')
#
#     num1 = int(input("Enter first Number: "))
#     num2 = int(input("Enter second Number: "))
#
#     if operation == '+':
#         if num1 == 56:
#             print("56 + 9 = 77")
#         else:
#             print(f"{num1} + {num2} = {num1 + num2}")
#     elif operation == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operation == '*':
#         if num1 == 45:
#             print("45 * 3 = 555")
#         else:
#             print(f"{num1} * {num2} = {num1 * num2}")
#     elif operation == '/':
#         if num1 == 56:
#             print("56/6 = 4")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#     elif operation == '**':
#         print(f"{num1} ** {num2} = {num1 ** num2}")
#     elif operation == '%':
#         print(f"{num1} % {num2} = {num1 % num2}")
#
# else:
#         print("You Press a Invalid Key")
#         again()
#
# def again():
#     cal_again = input('''
#     Do you want to calculate again?
#     Please type y for YES or n for NO.
#     ''')
#
#     if cal_again == 'y':
#         calculator()
#     elif cal_again == 'n':
#         print("See You Later")
#     else:
#         again()



          # OR

'''
# its definitely  work without any Query
# making a faulty calculator

# taking input from the user and changing into integer
inp1 = input("Operator")

# taking 2nd input from user
inp2 = input("First number")

# taking 3rd number
inp3 = input("Sceond number")

# making a new variable
new_input = inp2 + inp1 + inp3

# checking the input
if new_input == "45*3":
    print(555)
elif new_input == "56+9":
    print(77)
elif new_input == "56/6":
    print(4)
elif inp1 == "*":
    print(int(inp2) * int(inp3))
elif inp1 == "+":
    print(int(inp2) + int(inp3))
elif inp1 == "-":
    print(int(inp2) - int(inp3))
elif inp1 == "/":
    print(int(inp2) / int(inp3))
'''

