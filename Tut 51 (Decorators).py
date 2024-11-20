'''
Decorators in Python
'''

def function1():
    print("Subscirbe now")

func2 = function1             # here w're not putting parentesis bracket () in front of function1 coz it will call the function ,therefore we r only assignig this func1 to func2.,
del function1                   # even though after deleting func1 , it will print subscribe now coz it has copied in func2.
func2()


def funcret(num):                       #funcret here we r specifying function returner i.e. which return function.
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(1)
print(a)                             # here our conclusion is that we can use function to return function.



# ||| here we can - function ko as a  argument bhi likh sakte hai
# VVV

def executor(func):                 # yaha par bataya hai ki func k andar func bhi daal sakte hai as an argument.
    func("This")                    # aur func k dwara func ko return bhi kar sakte hai.

executor(print)




#_________________________Decorator function________________________________________

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_harry():
     print("Harry is a good boy")

who_is_harry()

who_is_harry = dec1(who_is_harry)     #<<<--- This line can be used as --->>>      @dec1   (but we have to write this dec1 above def function).
who_is_harry()