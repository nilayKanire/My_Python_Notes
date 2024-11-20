'''
Scope, Global Variables and Global Keyword
'''
# Scope

# def function1(n):
#      print(n, "I have printed")
#
# function1("This is me")             #Here 'n' value is "This is me" for function1


# Global Variables

#l = 10   # Global variable

# def function1(n):
#     l = 5       # Local variable
#     m = 8       # Local
#    # global l           # If local 'l' is not present in internal funtion & if we wanted to change global in funtion then we have to ask for permission and write global l.
#     l = l + 45           # <<--  If local 'l' is present in function then,this l can be changed only for local values only, not for global values .
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# print(l)


x = 89
def harry():                            # Function k andar function is called as Nasted function.
    x = 20
    def rohan():
        global x                                   #<<--  for this  global function to works there needs to be global variable outside the function like x = , print(x)
        x = 88
    print("before calling rohan()", x)                   # cltr + D to copy for the same statement in next line too.
    rohan()
    print("after calling rohan()", x)

harry()
print(x)