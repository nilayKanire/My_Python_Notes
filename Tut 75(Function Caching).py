'''
Function Caching IN Python
'''

import time
from functools import  lru_cache
'''
@lru_cache(maxsize=32)                # here maxsize is an argument . maxsize kya hota hai toh , aap kitni values ko cache karna chahte hai. hum jitni memory ko cache karenge vo hamari utni memory ko khayega.
def some_work(n):                   # cache value sidha retreive karlega function ke return value ko uski maxsize memory me se , aur hamara funtion repeatedly run karne ki jagah voh last time kiye gaye calls ko save kar lega apne cache memory me.
    #1 Some task taking  n  seconds
    time.sleep(n)
    return n

if __name__== '__main__':
    print("Now running some work")
    some_work(3)              # here 3 is seconds in time.
    some_work(2)
    some_work(1)
    some_work(4)
    print("Done... Calling again")
    input()
    some_work(3)               # yaha bhi vahi likhne se hame 3 sec ka delay milra output me, isliye humne lru_cache ka use kiya q ki hume delay  na mile.
    print("Called again")
'''
# quiz

inp = int(input("how many values do u want to cache\n"))
a = inp
@lru_cache(maxsize=a)
def doing_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now doing some work")
    inp1 = int(input("how many values do u want to cache\n"))
    doing_work(2)
    doing_work(1)
    doing_work(2)
    print(inp)
    doing_work(3)
    print("Work is done")

