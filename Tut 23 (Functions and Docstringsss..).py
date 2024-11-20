'''
Functions And Docstrings
'''

a = 9
b = 8
c = sum((a, b))           # built in function   #  Double parenthesis is necessary for this function and it is an imp. syntax in this.

print(c)

def function1 (a, b):                             # User define funtion (def) - This funtion define its user on its own.
    print("Hello you are in function 1", a+b)         #  Here Indentaion happens means funtion k ander ghusna
function1(a,b)
def function2(a, b):
    """This is a function which will calculate average of two numbers"""
    average = (a+b)/2
    print(average)
        #OR
    return average
function2(a,b)
    # we dont need to write Print before function
v = function2(5, 7)                 # If we store the function in variable then the funtion will give "None" in output.
print(v)                            # So if we want that the funtion will give something after writing line like 16 then we have to write "return average" for that to giving output.
print(function2.__doc__)                                  # and the funtion will be stored in V
# ^^^
# |||How to print a doc string. which we written in line 11.