'''
How to Find Execution Time of a Python Program Using Time Module
'''

from time import time

def fun1(a,b):
    #by Nilay Kanire
    return a+b

def func2(a,b):
    #by CodeWithHarry
    num1 = a
    num2 = b
    if(a>b and a!=3):
        sum([4,3])
        return a+b

# if __name__ == '__main__':
#     init = time()
#     for i in range(0, 56789):
#         fun1(3,5)
#     print("Nilay Kanire Time: ", time()-init )
#
#     init =time()
#     for i in range(0, 56789):
#         func2(3,5)
#     print("CodeWithHarry Time: ",time() - init )


if __name__ == '__main__':
    init = time()
    for i in range(0, 56789):
        fun1(3,5)


    for i in range(0, 56789):
        func2(3,5)
    print("Overall Time:  ",time() - init )