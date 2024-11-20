'''
Snake ,Water , Gun game using python
'''
'''
import random

print("Welcome to the snake water gun game\n")

print("you have 3 choices to choose \n"
      " snake(s)  water(w)   gun(g)\n")


list = ["snake","water","gun"]

snake = "snake"
water = "water"
gun  = "gun"

number_of_chance_to_play = 1
print("You can play 10 times in a row")

while (number_of_chance_to_play <= 10):
      chance_to_play = str(input())
      while (chance_to_play==snake):
            list = ["snake", "water", "gun"]
            choice = random.choice(list)
            print("\n Computer chooses :")
            print(choice)

            if choice == water:
                  print("you won")
                  break
            elif choice == gun:
                  print("you loose")
                  break
            else:
                  print("Draw")
                  break
            # print(10 - number_of_chance_to_play, "no. of chance left")
            # number_of_chance_to_play = number_of_chance_to_play + 1

      while (chance_to_play==water):
            list = ["snake", "water", "gun"]
            choice = random.choice(list)
            print("\n Computer chooses :")
            print(choice)

            if choice == snake:
                  print("you loose")
                  break
            elif choice == gun:
                  print("you won")
                  break
            else:
                  print("Draw")
                  break
            # print(10 - number_of_chance_to_play, "no. of chance left")
            # number_of_chance_to_play = number_of_chance_to_play + 1


      while (chance_to_play==gun):
            list = ["snake", "water", "gun"]
            choice = random.choice(list)
            print("\n Computer chooses :")
            print(choice)

            if choice == snake:
                  print("you won")
                  break
            elif choice == water:
                  print("you loose")
                  break
            else:
                  print("Draw")
                  break

      print(10-number_of_chance_to_play,"no. of chance left")
      number_of_chance_to_play = number_of_chance_to_play + 1

if(number_of_chance_to_play>10):
      print("Your chances to play ends")
'''


# Hi Harry Bhaiya , I'm in 10th class I've following your tutorial for last 2 weeks... Thanks a lot bhaiya
# Here is the " Snake , Water,  Gun "game with a complete new logic ...
# Subtraction results -  1      for win


'''
import time
import random
won_count = 0
Total_chances = 10
count = 0
User_name = input(""""        \n Welcome to Snake ,Water, Gun game ....
           You will be having 10 chances , if you win more than 5 times , you'll be declared as winner .....
            All the best ..{ENTER YOUR NAME HERE} : """)
def game():
    global User_name
    global won_count
    global Total_chances
    global count
    Machine_code = {"Snake": 4, "Water": 0, "Gun": 2}
    User_code = {"Snake": 1, "Water": 3, "Gun": 5}
    seq = ["Snake", "Water", "Gun"]
    while Total_chances !=0 :
        User_input = input(f"""\n{{ENTER YOUR CHOICE HERE}} chances left {Total_chances}: """)
        if User_input.lower().capitalize() in seq:
            Machine_choice = random.choice(seq)
            if User_input.lower().capitalize() == Machine_choice:
                print(f"    Oh its a tie ...I too have chosen {Machine_choice}")
                Total_chances -= 1
                continue
            elif (User_code[User_input.lower().capitalize()] - Machine_code[Machine_choice]) == -1 or (
                    User_code[User_input.lower().capitalize()] - Machine_code[Machine_choice]) == 5:
                # print(User_code[User_input.lower().capitalize()] - Machine_code[Machine_choice])
                print(f"You lose I had chosen {Machine_choice}")
                won_count -= 1
                Total_chances -= 1
            elif (User_code[User_input.lower().capitalize()] - Machine_code[Machine_choice]) == 1:
                # print(User_code[User_input.lower().capitalize()] - Machine_code[Machine_choice])
                print(f"\nWohoo.......!!!You won I had chosen {Machine_choice}")
                won_count += 1
                Total_chances -= 1
            count += 1

        else:
            print("some thing went wrong.. Input  error ")
            continue
    print("\n\n Game finished ..... Now its time for the result...")
    time.sleep(3)
    # print(won_count)
    if won_count > Total_chances//2:
        print("\nAnd now the winner is ....")
        time.sleep(2)
        print(f"None other than our {User_name} ")
    elif won_count == Total_chances//2:
        print("Its a tie")
        print(f"\n You played really very well {User_name} , better luck next time ..")
    else:
        print(f"\n\nComputer won , Don't worry {User_name} you will win next time")
game()
def after_game():
    global won_count
    global Total_chances
    global count
    final_input = input("\nWanna play again ? [Y/n] : ")
    if final_input.lower() == 'y':
        won_count = 0
        Total_chances = 10
        count = 0
        return game()
    else:
        print(f"Bye Bye {User_name} , Come back soon...")
after_game()
'''
'''
import random, playsound


def winning_music():
      """
      Plays the winning music.
      """
      win_music = ["anime wow.mp3", "bruhh.mp3"]
      try:
            playsound.playsound(random.choice(win_music))
      except Exception as e:
            print(e)


def losing_music():
      """
      Plays the losing music.
      """
      lose_music = ["Nope.mp3", "Fart.mp3"]
      try:
            playsound.playsound(random.choice(lose_music))
      except Exception as e:
            print(e)


def tie_music():
      """
      Plays the tie music.
      """
      try:
            playsound.playsound("Awkward Cricket.mp3")
      except Exception as e:
            print(e)


if __name__ == "__main__":
      print("\nWelcome to the Snake Water Gun game!\n\n")
      attempts = 1
      your_point = 0
      computer_point = 0
      while (attempts <= 10):
            lst = ["s", "w", "g"]
            ran = random.choice(lst)

            inp = input("Enter your choice (Snake(s), Water(w), Gun(g)): ")
            inp = inp.lower()

            if inp == 's' and ran == 's':
                  if inp == ran:
                        print("Tie")
                        print(f"\nYou chose snake and Computer also chose snake! ")
                        print("No body gets point\n")
                        tie_music()


                  elif inp == 'w' and ran == 'w':
                        print("Tie")
                        print(f"\nYou chose water and Computer also chose water! ")
                        print("No body gets point\n")
                        tie_music()


                  elif inp == 'g' and ran == 'g':
                        print("Tie")
                        print(f"\nYou chose gun and Computer also chose gun! ")
                        print("No body gets point\n")
                        tie_music()


                  elif inp == "s" and ran == "w":
                        your_point = your_point + 1
                        print(f"\nYou choosed snake and Computer chose water! ")
                        print("The snake drank water\n")
                        print("You won this round")
                        print("You got 1 point\n")
                        winning_music()
                  elif inp == "w" and ran == "s":
                        computer_point = computer_point + 1
                        print(f"\nYou choosed water and Computer chose snake! ")
                        print("The snake drank water\n")
                        print("You lost this round")
                        print("Computer gets 1 point\n")
                        losing_music()
                  elif inp == "w" and ran == "g":
                        print(f"\nYou chose water and Computer chose gun! ")
                        your_point = your_point + 1
                        print("The gun sank in water\n")
                        print("You won this round")
                        print("You got 1 point\n")
                        winning_music()
                  elif inp == "g" and ran == "w":
                        print(f"\nYou choosed gun and Computer chose water! ")
                        computer_point = computer_point + 1
                        print("The gun sank in water\n")
                        print("You Lost this round")
                        print("computer gets 1 point\n")
                        losing_music()
                  elif inp == "g" and ran == "s":
                        print(f"\nYou choosed gun and Computer chose snake! ")
                        your_point = your_point + 1
                        print("The snake was shot and it died\n")
                        print("You won this round")
                        print("You get 1 point\n")
                        winning_music()
                  elif inp == "s" and ran == "g":
                        print(f"\nYou choosed snake and Computer chose gun! ")
                        computer_point = computer_point + 1
                        print("The snake was shot and he died\n")
                        print("You lost this round!")
                        print("Computer gets 1 point\n")
                  else:
                        print("Invalid input!\n")
                        continue
            print("\nNo. of guesses left: {}".format(10 - attempts))
            attempts = attempts + 1
            if attempts > 10:
                  print("\nGame over!\n")
      print(f"Your score: {your_point} \nComputer's score: {computer_point}")
      if computer_point > your_point:
            print("\nComputer won and you lost!\n")
      elif computer_point < your_point:
            print("\nYou won and computer lost!\n")
      else:
            print("It was a tie!")
            print("Invalid")
      print(11 - attempts, "no. of guesses left")
      attempts = attempts + 1
      if attempts > 10:
            print("\nGame over! ")
if computer_point > your_point:
      print("\nComputer wins and you lose!")
if computer_point < your_point:
      print("\nYou win and the computer loses!")
print(f"\nYour points are {your_point} and Computer's points are {computer_point}!\n")
'''


#
# Aritra Roy
# 11 months ago
#Exercise 6: Game Development: Snake Water Gun

import random
print("The game will be total of 10 rounds\nPress: 's' for Snake or 'w' for Water or 'g' for Gun")
i=0
win=0
lost=0
draw=0
while i<10:
    lst=["Snake", "Water", "Gun"]
    choice=random.choice(lst)
    n=input("\nEnter your choice: ")
    if choice=="Snake":
        if n=="s":
            print("Computer's choice: ",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    elif choice=="Water":
        if n=="w":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    else:
        if n=="g":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    print("Left-over round number: ",10-i)
    a=f"\nTill now the score is:\nYou: {win}\nComputer: {lost}\nDraw: {draw}"
    print(a)
    i+=1
if i==10:
    if win>lost:
        print("\nWinner!!! You have won the game")
    elif lost>win:
        print("\nGame Over!!! You have lost the game")
    else:
        print("\nGame Draw!!!")

