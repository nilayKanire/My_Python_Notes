'''
*args and **kwargs In Python
'''

'''
1. *args
'''

def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e )

function_name_print("Harrry", "Rohan", "Skillf", "Hammad", "Shivam" )
# THis above method cant be used for adding hundreds of user , therefore we use *args and **kwargs


def funargs(*args):
    print(type(args))             # Type of arg is tupple , if our input is in list [] or tupple () form , the output will be tupple ().
    print(args[1])

    har = ["Harry", "Rohan", "Skillf", "Hammad", "Nilay"]
    funargs(*har)
    return
# funargs(*args)
# This above programm will give us a output name in horizantal line


# def funargs(normal, *argsHarsh):
#     print(normal)
#     for item in argsHarsh:                # Due to for item  in , line our output names will be displayed vertical line by line.#
#      print(item)
# har = ["Harry", "Rohan", "Skillf", "Hammad" , "Nilay ", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# funargs(normal, *har)

#      ^^^
#      |||______ For *args we have to put normal first then *args
#                EX:- def funargs(normal, *argsHarsh):
#                If we put normal after args func. then it will show error.
'''
2. *kwargs
'''
def funargs(normal, *argsHarsh, **kwargs):            # *args & **kwargs are optional if we want to use then use otherwise don't use.
    print(normal)

    for item in argsHarsh:
     print(item)
    print("\nNow I would Like to introduce some of our heroes\n")
    for key, value in kwargs.items():
        print(f"{key} is a  {value}")

har = ["Harry", "Rohan", "Skillf", "Hammad" , "Nilay ", "The programmer"]
normal = "I am a normal Argument and the students are:"
#funargs(normal)

kw = {"Rohan":"Monitor", "HarrY":"Fitness Instructor",
      "The Programmer":"Nilay", "Shivam":"Cook"}
funargs(normal, *har , **kw)