import time
import os
# import art


def welcome():
    os.system("clear")
    welcome = print("""
    *********************************************
    Welcome to your best and newest Pomodoro app!
    *********************************************
    """)
   

welcome()

# Keeps track of number of study times
study_times = 0
# 25 minute timer
# dont forget to change run time
def work_timer():
    global study_times
    minutes = 0
    print("25 minute timer starts now!")
    while minutes <= 1:
        time.sleep(60)
        minutes = minutes + 1
        study_times =+ 1
    print(f"{study_times} study times completed... Time for a break!")

# 5 minute timer
# dont forget to change run time
def break_timer():
    global study_times
    minutes = 0 
    if study_times <4:
        print("5 minute break! Let's go!")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("break over :( ")
    elif study_times == 4:
        print("You've earned a long break.")
        while minutes != 1:
            time.sleep(60)
            minutes = minutes + 1
            print("long break over :( ")
        study_times = 0



work_start = input("Press enter to begin 25 minute work timer: ")
break_start = input("Press enter to start break timer")
print(study_times)

def pomodoro():
    print(work_start)
    work_timer()
    print(break_start)
    break_timer()

pomodoro()