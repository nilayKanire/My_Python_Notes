"""
Using with Block To Open Python Files
"""

f = open("harry.txt", "rt")
print(f.readlines())
print(f.readline())

f.close()

with open("harry.txt") as f:                   # This 'with and as' function is equals to f=open() and f.close()
    a = f.read(4)
    print(a)

"""
'Question of the day - yes or No'

Yes, It will be executed Because.File is automatically closed when we open with with block. Another reason can be we are opening file again.
"""