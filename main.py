import time
import os
from random import choice
from art import *

# prints pomodoro x friendo ascii art heading
def heading():
    header = text2art("Pomodoro X Friendo", font="small")
    print(header)

# welcome message to explain whhat the app does
def welcome():
    # clears terminal window
    os.system("clear")
    #prints pomodoro x friendo ascii
    heading()
    greeting_2 = print('''
    This application allows you to run a pomodoro app with a little bit of added motivation.
    Meet your new best motivational buddy! You can give them whatever name you like down below.

    As the work and break timer run, your friendo's happiness will go up! 
    If your friendo has to wait for your command, their happiness will go down, down, down...

    Check on their mood at any time by typing "friendo".

    if you get stuck, type "help".

    Have fun!!!
    
    ''')


# Keeps track of number of times work_timer has run
study_times = 0

# 25 minute timer
def work_timer():
    global study_times
    global pet_mood
    # saves current time to be deducted later
    happy_timer = time.time()
    minutes = 0
    print("25 minute timer starts now!\n")
    # counts up for every .sleep() cycle
    while minutes <= 25:
        time.sleep(60)
        minutes = minutes + 1
    study_times += 1
    if study_times < 4:
        print(f"{study_times} study times completed... \nTime for a break!\n")
    # runs if work_timer has run 4 times
    else:
        print(f"{study_times} completed! Time for a 15 minute break!\n")
    # stops timer, returns an int and adds points to pet_mood
    end_happy = time.time() - happy_timer
    pet_mood += end_happy // 10

# 5 minute timer
# dont forget to change run time
def break_timer():
    global study_times
    global pet_mood
    # saves current time to be deducted later
    happy_timer = time.time()
    minutes = 0 
    if study_times <4:
        print("5 minute break! Let's go!\n")
        # runs 5 minute break timer
        while minutes != 5:
            time.sleep(60)
            minutes = minutes + 1
            print("break over :( \n")
        # ends timer to and adds into to pet_mood
        end_happy = time.time() - happy_timer
        pet_mood += end_happy // 10
    elif study_times == 4:
        print("You've earned a long break.\n")
        # runs a 15 minute timer if work_timer has run 4 times
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("long break over :( \n")
        #resets study times back to 0
        study_times = 0
        # ends timer to and adds into to pet_mood
        end_happy = time.time() - happy_timer
        pet_mood += end_happy // 10

#tuple of affirmations to be called with user_input
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
#the three moods of your friendo pet
happy_pet = "(　＾∇＾)"
neutral_pet = "ƪ(‾ε‾“)ʃ"
sad_pet = ".·´¯`(>▂<)´¯`·." 
pet_mood = 500
#prints different result depending on pet_mood score
def your_pet():
    if pet_mood <= 333:
        print(f"{name} is a bit sad {sad_pet}")
    elif pet_mood <= 666:
        print(f"{name} is a doing ok {neutral_pet}")
    else:
        print(f"{name} is a super happy! {happy_pet} Great job!")

#prints list of commands after user_input help
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
name = ""
#while loop and try/except block allow app to fail gracefully afet keyboard innterrupt
while name == "":
    try:
        welcome()
        heading()
        name = str(input("Name your pet: \n"))
        your_pet()
        help()
    except KeyboardInterrupt:
        print("Gone so soon???")
        exit()

#main user interface, takes any of the seven commands and returns the appropriate function
while user_input != "bye":
    try:
        #starts timer to count reduce pet_mood while waiting for input
        sad_timer = time.time()
        user_input = input("enter a command: \n")
        #ends timer after user_input and deducts from pet_mood
        end_sad = time.time() - sad_timer
        pet_mood -= end_sad // 5
        # starts work timer
        if user_input == "work":
            work_timer()
        #starts break timer
        elif user_input == "break":
            break_timer()
        # shows your friendo's mood
        elif user_input == "friendo":
            your_pet()
        # pulls a random affirmation from the tuple
        elif user_input == "vibe check":
            affirm_tuple()
            print("(づ￣ ³￣)づ ")
        #prints list of usable commands
        elif user_input == "help":
            help()
        #exits app
        elif user_input == "bye":
            print("See you next time!")
        # ckears terminal screen and prints heading function so the user knows they're still in the app
        elif user_input == "clear":
            os.system("clear")
            heading()
        #if user input isnt one of the above, lets the user know its incorrect
        else:
            print("I dont know that command...type 'help' if you're stuck")
        #allows program to fail gracefully with kewboard interrupt
    except KeyboardInterrupt:
        print("\nGreat work today!!!")
        exit()

#no code beyond here
#only darkness awaits