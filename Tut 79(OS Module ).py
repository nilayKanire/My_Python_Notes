'''
Os  Module In Python
'''

import os

print(dir(os))
print(os.getcwd())              # cwd here is current working directory.

os.chdir("c://")              # chdir here full form is change directory. of os module.
print(os.getcwd())            # current working directory bahut jaroori hota hai q ki hum jab code likhre ho to vo usi directory me hona chahiye jaha code read ya work karwana ho.

# f = open("harry.txt")

print(os.listdir())              # listdir hume 'directory ki list' de raha hai saare k saare jo bhi exist karte honge uss list k andar
print(os.listdir("c://"))
print(type(os.listdir("c://")))

os.mkdir("This")          # mkdir - folder banata hai . I think mk means make.m
os.makedirs("This/that")          # makedirs create a folder "This" and then ' That' sub-folder(sub-directory) is also  created inside 'This'.

# os.rename("harry.txt", "code with harry.txt")

print(os.environ.get('Path'))      # ye environment variable read karta hai. iske andar path likhne se hume 'Path' naam ka environment variable mila hai.

# print(os.path.join("c://", "/harry.txt"))       # isme path ko join kar rahe hai aur jo bhi slashes ya kuch extra ka hota hai voh hatadeta hai.

os.path.exists("c://")
print(os.path.exists("c://"))

print(os.path.isdir("c://"))
print(os.path.isfile("c://"))
