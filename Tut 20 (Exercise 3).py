"""
Guess The Number
"""
# n = 18
# no of guesses
# print no of guesses left
# No of guesses he took to finish
# game over

print("Guess the number")

n = 18
no_of_guess = 9

while(True):
    no_of_guess = no_of_guess - 1
    num = int(input("Enter the number \n"))
    if no_of_guess > 0:
        if num > n:
            print("Guessed no. is greater than the actual no. ")
            print("No. of guesses left is",no_of_guess)

        elif num < n:
            print(" Guessed no. is lesser than the actual no. ")
            print("No. of guesses left is",no_of_guess)

        else:
            print(" you Guessed the correct no.")
            print("No. of guesses left you took is ",no_of_guess)
            break


    elif no_of_guess == 0:
        print("you used all the guess You lost \n no. of guess left is", no_of_guess)





















'''
print("Guess The Number ")
print("You have only 5 guesses to guess the Actual Number")
print("Enter the Number")

n1 = 18
n2 = int(input())
n3 = n2
while(True):
    print()
    if n2<18:
       print("No wrong guess","\n Your guessed no.is smaller than the Actual Number")
       print("Try again")
       n1 = 18
       break


    elif n2==18:
        print("Yes, Your guess is correct")
        print("you win")
        n1 = 18
        break

    else:
        print("No wrong guess"," \nYour guessed no. is greater than the Actual Number")
        print("Try again")
        n1 = 18
        break
'''
               #OR
'''
#Solution
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter lesser number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
'''












# print("guess the number")
# print("You have only 5 gussess to guess the actual number")
# n1 = 18
# n2 = int(input())
#
# while(True):
#     if n2 == n1:
#         print("your guess is correct ")
#         break
#
#     elif n2 > n1:
#         print("your guess no. is wrong and it is greater than actual no.")
#
#         print("guess the no. again")
#
#     elif n2 < n1:
#         print("your guess no. is wrong and it is lesser than the actual no.")
#
#         print("guess the no. again")
#


