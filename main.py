import time
import os
from random import choice
from art import *



def welcome():
    os.system("clear")
    heading()
    greeting_2 = print('''
    This application allows you to run a pomodoro app with a little bit of added motivation.
    Meet your new best motivational buddy! You can give them whatever name you like down below.

    As you the work and break timer run, your friendo's happiness will go up! 
    If your friendo has to wait for your command, their happiness will go down, down, down...

    Check on their mood at any time by typing "friendo".

    if you get stuck, type "help".

    Have fun!!!
    
    ''')
    help()

def heading():
    header = text2art("Pomodoro X Friendo", font="small")
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

happy_pet = "(　＾∇＾)"
neutral_pet = "ƪ(‾ε‾“)ʃ"
sad_pet = ".·´¯`(>▂<)´¯`·." 
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
    Check on your buddy: "friendo"
    Need a little confidence boost: "vibe check"
    Exit the application: "bye"
    List of commands: "help"
    ''')


user_input = ""
welcome()
heading()
name = str(input("Name your pet: \n"))
your_pet()


while user_input != "bye":
    try:
        sad_timer = time.time()
        user_input = input("enter a command: \n")
        end_sad = time.time() - sad_timer
        pet_mood -= end_sad // 5
        print(pet_mood)
        if user_input == "work":
            work_timer()
        elif user_input == "break":
            break_timer()
        elif user_input == "buddy":
            your_pet()
        elif user_input == "vibe check":
            affirm_tuple()
            aprint("hugs")
        elif user_input == "help":
            help()
        elif user_input == "bye":
            print("See you next time!")
        elif user_input == "clear":
            os.system("clear")
            heading()
        else:
            print("I dont know that command...type 'help' if you're stuck")
    except KeyboardInterrupt:
        print("\nGreat work today!!!")
        exit()