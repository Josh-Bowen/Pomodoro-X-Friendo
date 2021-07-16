import time
import os
from random import choice
from art import *


def welcome():
    os.system("clear")
    print("""
    *****************************************************
    ****Welcome to your best and newest Pomodoro app!****
    *****************************************************
    """)
    help()

def heading():
    header = text2art("Pomodoro X Friendo")
    print(header)

# Keeps track of number of study times
study_times = 0
# 25 minute timer
# dont forget to change run time
def work_timer():
    global study_times
    global pet_mood
    happy_timer = time.time()
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
    end_happy = time.time() - happy_timer
    pet_mood += end_happy // 10

# 5 minute timer
# dont forget to change run time
def break_timer():
    global study_times
    global pet_mood
    happy_timer = time.time()
    minutes = 0 
    if study_times <4:
        print("5 minute break! Let's go!\n")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("break over :( \n")
        end_happy = time.time() - happy_timer
        pet_mood += end_happy // 10
    elif study_times == 4:
        print("You've earned a long break.\n")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("long break over :( \n")
        study_times = 0
        end_happy = time.time() - happy_timer
        pet_mood += end_happy // 10

def affirm_tuple():
    my_tuple = (
        "You're doing a great job!",                        #0
        "Well done! Keep it up!",                           #1
        "Keep going ya cutey!",                             #2
        "10/10 effort! Don't quit now!",                    #3
        "You can do this!",                                 #4
        "Times might be tough, but it is not permanent.",   #5
        "You can and you will(do the thing)!",              #6
        "*slow clap*",                                      #7
        "Be proud of yourself! You're wonderful!",          #8
        "Making mistakes are the best way to learn.",       #9 
    )
    print(choice(*my_tuple))



#this is your python pet

happy_pet = ":)"
neutral_pet = ":|"
sad_pet = ":("
pet_mood = 500

def your_pet():
    if pet_mood <= 333:
        print(f"{name} is a bit sad {sad_pet}")
    elif pet_mood <= 666:
        print(f"{name} is a doing ok {neutral_pet}")
    else:
        print(f"{name} is a super happy! {happy_pet} Great job!")


def help():
    print(''' Here is a list of commands:
    Start work timer: "work"
    Start break timer: "break"
    Check on your buddy: "buddy"
    Need a little confidence boost: "vibe check"
    Exit the application: "bye"
    List of commands: "help"
    ''')



user_input = ""
welcome()
name = str(input("Name your pet: \n"))
your_pet()

while user_input != "bye":
    try:

        user_input = input("enter a command: \n")
        if user_input == "work":
            work_timer()
        elif user_input == "break":
            break_timer()
        elif user_input == "buddy":
            your_pet()
        elif user_input == "vibe check":
            affirm_tuple()
        elif user_input == "help":
            help()
        elif user_input == "bye":
            print("See you next time!")
        elif user_input == "clear":
            os.system("clear")
        else:
            print("I dont know that command...type 'help' if you're stuck")
    except KeyboardInterrupt:
        print("\nGreat work today!!!")
        exit()