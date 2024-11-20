'''
Writing And Appending To A File
'''

#  Append means joinning , it joins the any Text at the end of a file.

# f = open("harry2.txt", "w")                     # f is file handler    # If we write name of a file same to other than our content will replace the old file content with new content of file with the same name.
# f.write("Harry bhai bahut achhe hain")
# f.close()

'''
Append
'''
f = open("harry2.txt", "a")
a = f.write("Harry bhai bahut achhe hain\n")               # If we repeatedly run this append programm then it will repeatedly add on the same conent again and again.
print(a)                                                    # Here we customize code to know how many letters there in file
f.close()                                                  # Thats why we put a =    and print(a) in a code
'''
Handle  read and write both       # here we are using read and write mode together in a file.
symbol is "r+" meaning we want to read and write the file both.
'''

f = open("harry2.txt", "r+")
print(f.read())
f.write("Thank you")