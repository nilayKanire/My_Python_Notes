"""
Break and Continue statements in Python
"""
i = 0

#while(i<45):
 #   print(i+1)
  #  i = i + 1

# while(True):
#     print(i+1, end=" ")
#     if(i==44):
#      break      #stop the loop
#     i = i + 1
# yaha par

while(True):
    i = i + 1
    if i+1<5:
        continue                    # when the above written condition becomes true for i ,then the programm will.
                                   # again go to upwards code and again check the condition . But when the " i "condition
                                   # doesnt met the above code then the programm will forwarded to the below written code.
    print(i+1, end=" ")
    if(i==44):
            break



"""
Quiz|||
    VVV
"""
while(True):
    inp = int(input("\nEnter a Number\n"))                   # \n is a New line character.
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
