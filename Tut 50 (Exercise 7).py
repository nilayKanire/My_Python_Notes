'''
Healthy Programmer
'''

'''
9am - 5pm
Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
Physical Acitvity - physical.mp3 every - 45 min - ExDone - log
'''
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time



def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
         input_of_user = input()
         if input_of_user == stopper:
             mixer.music.stop()
             break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    #musiconloop("drink-water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 4*6
    eyessecs = 3*3
    exsecs = 5*6

# print("Healthy Programmer schedule")
#
# print("shcedule starts today from 9am & end at 5pm")
#     if x.hour >= 9 and x.hour <= 17:
while True:
    if time() - init_water > watersecs:
        print("Water Drinking time . Enter 'drank' to stop the alarm.")
        musiconloop("drink-water.mp3",'drank')
        init_water = time()
        log_now("Drank Water at")

    if time() - init_eyes > eyessecs:
        print("Eye Exercise time . Enter 'done eyes' to stop the alarm.")
        musiconloop("eye-blink-sound.mp3",'done eyes')
        init_eyes = time()
        log_now("Eyes Relaxed at")

    if time() - init_exercise > exsecs:
        print("Physical Activity time . Enter 'donephy' to stop the alarm.")
        musiconloop("workout.mp3",'donephy')
        init_exercise = time()
        log_now("Physical Activity Done  at")
    # elif x.hour <= 9 and x.hour >= 17:
    #     print("Schedule Ended")
    #     pass
    #     # elif (x.minute <= 1 and x.hour < 9) or (x.hour > 16 and x.minute >= 1):
    #     #     print("no, schedule ended")








'''
def gettime():
    return datetime.datetime.now()
x = datetime.datetime.now()
# variables for time
d = x.strftime("%d")
h = x.strftime("%H")
m = x.strftime("%M")
w = x.strftime("%w")
am_pm = x.strftime("%p")
time =x.strftime(f"day is {d} , Hour is {h} {am_pm} and minute is {m}")
print(time)

# variables for water
m1 = x.minute % 20
# Variable for Exercise
e1 = x.minute % 45

print("Healthy Programmer schedule")

if x.day >= 1:
    print("shcedule starts today from 9am & end at 5pm")
    if x.hour >= 9  and x.hour <= 23:
        if m1 == 0:
            print("Time to drink water")

            def add_func(client):
                if client == "1":
                    drink_water = input("Enter number 1 for drink water or 2 for log of drinking time : ")
                    add_item = input("What do you want to Add? : ")
                    if drink_water == "1":
                        with open("Nilay_drinkwater.txt", "a") as f:
                            add = [" [", x, "] ", add_item, "\n"]
                            for item in add:
                                f.write("%s" % item)
                        print("Item successfully added")
                    elif drink_water == "2":
                        with open("Nilay_logof_drinkingtime.txt", "a") as f:
                            add = [" [", x, "] ", add_item, "\n"]
                            for item in add:
                                f.write("%s" % item)
                        print("Item successfully added")


            def retrieve_func(client):
                if client == "1":
                    drink_water = input("Enter number 1 for drink water or 2 for  log of drinking time : ")
                    if drink_water == "1":
                        try:
                            with open("Nilay_drinkwater.txt", "r") as f:
                                print("\nFile items\n")
                                for i in (f.readlines()):
                                    print(i)
                        except:
                            print("Items does not retrieve. Please add some items in file")

                    elif drink_water == "2":
                        try:
                            with open("Nilay_logof_drinkingtime.txt", "r") as f:
                                print("\nFile items\n")
                                for i in (f.readlines()):
                                    print(i)
                        except:
                            print("Items does not retrieve. Please add some items in file")


            client = input("Enter number 1 for Nilay:  ")
            add_retrieve = input("Enter number 1 for Add and 2 for Retrieve :  ")

            if add_retrieve == "1":
                add_func(client)
            elif add_retrieve == "2":
                retrieve_func(client)



        elif m1 != 0:
            print("Time to drink water is yet to come")

            def add_func(client):
                if client == "1":
                    drink_water = input("Enter number 1 for drink water or 2 for log of drinking time : ")
                    add_item = input("What do you want to Add? : ")
                    if drink_water == "1":
                        with open("Nilay_drinkwater.txt", "a") as f:
                            add = [" [", x, "] ", add_item, "\n"]
                            for item in add:
                                f.write("%s" % item)
                        print("Item successfully added")
                    elif drink_water == "2":
                        with open("Nilay_logof_drinkingtime.txt", "a") as f:
                            add = [" [", x, "] ", add_item, "\n"]
                            for item in add:
                                f.write("%s" % item)
                        print("Item successfully added")


            def retrieve_func(client):
                if client == "1":
                    drink_water = input("Enter number 1 for drink water or 2 for  log of drinking time : ")
                    if drink_water == "1":
                        try:
                            with open("Nilay_drinkwater.txt", "r") as f:
                                print("\nFile items\n")
                                for i in (f.readlines()):
                                    print(i)
                        except:
                            print("Items does not retrieve. Please add some items in file")

                    elif drink_water == "2":
                        try:
                            with open("Nilay_logof_drinkingtime.txt", "r") as f:
                                print("\nFile items\n")
                                for i in (f.readlines()):
                                    print(i)
                        except:
                            print("Items does not retrieve. Please add some items in file")


            client = input("Enter number 1 for Nilay:  ")
            add_retrieve = input("Enter number 1 for Add and 2 for Retrieve :  ")

            if add_retrieve == "1":
                add_func(client)
            elif add_retrieve == "2":
                retrieve_func(client)


    elif x.hour <= 9 and x.hour >=23:
        print("Schedule Ended")
        pass
        # elif (x.minute <= 1 and x.hour < 9) or (x.hour > 16 and x.minute >= 1):
        #     print("no, schedule ended")

if x.day >= 1:
    print("shcedule starts today from 9am & end at 5pm")
    if x.hour >= 9  and x.hour <= 23:
        print("Now Schedule for exercise")
        if e1 == 0:
            if e1==15:
                if e1 == 30:
                    print("Time to exercise")

        else:
            print("Time to drink water is yet to come")

    elif x.hour <= 9 and x.hour >=23:
        print("Schedule Ended")

'''



