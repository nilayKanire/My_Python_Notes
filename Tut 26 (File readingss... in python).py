'''
Open(), Read() & Readline() For Reading File IN Python
'''

# Read mode & Text mode are --->>> default mode
# f = open("harry.txt")            # inside the bracket written is File name which is existing.
#   ----------------------------------------
#                    |||_____________________________ This upper line is pointer Open() which pointing a file we were written in it.

# f = open("harry.txt", "rb")                      # we are reading the file in 'rb' argument mode means read in binary and read  If we only written 'r' then it will read in normal form.
# content = f.read()
# print(content)

# f.close()

#f = open("harry.txt", "rt")        # rt is default read text mode.
# content = f.read(34455)            # this line will print the 34455 characters in file
# print("1", content)                # Here we written '1' before  because the system will written only first 34455 charaters .

# content = f.read(34455)            # And by writing this double this line will print the next 34455 characters in file.
# print("2", content)                # here we written '2' before because the system will written the next characters after first 34455 characters is printed
# f.close()

f = open("harry.txt", "rt")
content = f.read()
for line in f:                # By  this we can read out content line by line.
     print(line)
     print(line, end="")      # the output is  line by line written like new line character is inbuilt in this code.

f =  open("harry.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())

print(f.readlines())       #<<<--- In this line output it is shown  where we used 'New line character' in our harry.txt file
f.close()