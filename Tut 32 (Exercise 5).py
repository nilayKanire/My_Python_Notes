# Health Management System
# 3 clients - Harry , Rohan and Hammad
# we have to manage this clients diet and Exercise.
# we have to make 3 files for there food log and 3 files for there exercise log.

# Total 6 files
# write a function that when executed takes as input client name
# one more funtion to retrieve exercise or food for any client

inp = str(input("Enter your Name\n"))

inp2 = str(input("Do you want to 'log' the file or 'retrieve'?\n"))
if inp2 == "retrieve" or inp2 == "Retrieve":
    def retrieve_file(inp):
        if inp == "Harry" or inp == "harry":
            filename = str(input("Enter the file name which you want to open\n Exercise or Diet\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("harry_exer.txt","r")
                print(fe.read())
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("harry_diet.txt","r")
                print(fd.read())
                fd.close()
        elif inp == "Rohan" or inp == "rohan":
            filename = str(input("Enter the file name which you want to open\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("Rohan_Exercise.txt","r")
                print(fe.read())
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("RohanDiet.txt", "r")
                print(fd.read())
                fd.close()
        elif inp == "Hammad" or inp == "hammad":
            filename = str(input("Enter the file name which you want to open\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("hammad_exer.txt", "rx")
                print(fe.read())
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("hammad_diet.txt", "rx")
                print(fd.read())
                fd.close()
        return
    retrieve_file(inp)
elif inp2 == "Log" or inp2 == "log":
    def log_file(inp):
        if inp == "Harry" or inp == "harry":
            filename = str(input("Enter the file name which you want to open\n Exercise or Diet\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("harry_exer.txt","a")
                fe.write(str(input()))
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("harry_diet.txt","ax")
                fd.write(str(input()))
                fd.close()
        elif inp == "Rohan" or inp == "rohan":
            filename = str(input("Enter the file name which you want to open\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("Rohan_Exercise.txt","a")
                fe.write(str(input()))
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("RohanDiet.txt", "a")
                fd.write(str(input()))
                fd.close()
        elif inp == "Hammad" or inp == "hammad":
            filename = str(input("Enter the file name which you want to open\n"))
            if filename == "Exercise" or filename == "exercise":
                fe = open("hammad_exer.txt", "ax")
                fe.write(str(input()))
                fe.close()
            elif filename == "Diet" or filename == "diet":
                fd = open("hammad_diet.txt", "ax")
                fd.write(str(input()))
                fd.close()

        return
    log_file(inp)



























'''
def getdate():
    import datetime
    return datetime.datetime.now()

print("Enter the number as per given to ur name")
var1 = 1
var2 = 2
var3 = 3

num  = int(input())

if num ==var1:
    print("Name is Harry\n")
    log1 = str(input("What do you want ,\n"
                     " log or retrieve ?\n"))

elif num ==var2:
    print("Name is Rohan\n")

elif num == var3:
    print("Name is Hammad\n")
'''
'''

#bhai ye rha program
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("health management system: ")
a=int(input("press 1 for log the value and 2 for retrieve \n"))

if a==1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad\n "))
    take(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad \n"))
    retrieve(b)

'''

# Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - Harry, Rohan and Hammad
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client
'''
import datetime

def getdate():
    return datetime.datetime.now()

def add_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("harry_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("harry_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")          
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("rohan_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("rohan_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("hammad_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("hammad_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added") 
def retrive_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("harry_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")        
        elif exer_diet == "2":
            try:
                with open("harry_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i) 
            except:
                print("Items does not retrieve. Please add some items in file")                
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("rohan_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("rohan_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("hammad_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("hammad_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")          

client = input("Enter number 1 for harry, 2 for rohan and 3 for hammad : ") 
add_retrieve = input("Enter number 1 for Add and 2 for Retrieve : ")

if add_retrieve == "1":
    add_func(client)
elif add_retrieve == "2":
    retrive_func(client)
'''