'''
Seek(), tell() & More On Python Files
'''

f = open("harry2.txt")
f.seek((12))
print(f.tell())             # The f.tell() is function which tells us where is our file pointer means it shows on which character it is on.

print(f.readline())
print(f.tell())
##f.seek(11)                  # This function resets  our file pointer bring back to a position which we are inputing in this function.
print(f.readline())
print(f.tell())
f.close()