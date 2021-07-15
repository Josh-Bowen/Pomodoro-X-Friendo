import time
import os
# import art


def welcome():
    os.system("clear")
    welcome = print("""
    *****************************************************
    ****Welcome to your best and newest Pomodoro app!****
    *****************************************************
    """)

# Keeps track of number of study times
study_times = 0
# 25 minute timer
# dont forget to change run time
def work_timer():
    global study_times
    minutes = 0
    print("25 minute timer starts now!\n")
    while minutes <= 1:
        time.sleep(60)
        minutes = minutes + 1
    study_times += 1
    if study_times < 4:
        print(f"{study_times} study times completed... \nTime for a break!\n")
    else:
        print(f"{study_times} completed! Time for a 15 minute break!\n")

# 5 minute timer
# dont forget to change run time
def break_timer():
    global study_times
    minutes = 0 
    if study_times <4:
        print("5 minute break! Let's go!\n")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("break over :( \n")
    elif study_times == 4:
        print("You've earned a long break.\n")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("long break over :( \n")
            study_times = 0




# after any timer runs, happiness gets a boost of points,
# then while program is waiting for input, happiness ticks down every second or so...


#this is your python pet

happy_pet = ":)"
neutral_pet = ":|"
sad_pet = ":("
name = str(input("Name your pet: \n"))

def your_pet():
    name.capitalize()
    pet_mood = 50
    if pet_mood <= 33:
        print(f"{name} is a bit sad {sad_pet}")
    elif pet_mood <= 66:
        print(f"{name} is a doing ok {neutral_pet}")
    else:
        print(f"{name} is a super happy! {happy_pet} Great job!")
 
# def pet_mood():
   
        


while True:
    start = time.time()
    work_timer()
    end = time.time() - start
    points_down = int(end)
    print(points_down)

