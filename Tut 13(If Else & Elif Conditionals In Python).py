"""
If Else & Elif Conditionals in Python
"""
#var1 = 6
#var2 = 56
#var3 = int(input())

#if var3>var2:                       # collan( : ) - if we put collan at end then it means we want to enter inside this ' if ' statement.
 #   print("Greater")                # After that "indentation" occurs and it creates a tab(space) automatically and our code will enter inside the statement
#elif var3==var2:                      # use 2 times equal to ( == ) sign when we are showing its equal
  #  print("Equal")
#else:
 #   print("Lesser")
"""
IN keywords
"""
list1 = [5, 7, 3]
print(5 in list1)
if 5 in list1:
        print("Yes its in the list")

    # Not and In are two different keywords!

"""
NOT In - keywords
"""
#list1 = [5, 7 ,3]
#print(15 not in list1)
#if 15 not in list1:
  #  print("NO its not in the list")
"""
    |||   QUiZ 
    VVV
"""
print("Enter your age")
var1 = 18

var4 = int(input())

if var4<var1:
     print("You cannot drive")
elif var4==var1:
    print("You come here and we will see u can drive or not?")
else:
    print("YOu can drive")

        # OR

print("What is your age?")
age = int(input())
if age<18:
    print("You cannot drive")

elif age==18:
    print("We will think about you")

else:
    print("You can drive")



