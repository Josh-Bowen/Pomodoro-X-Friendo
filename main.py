import time
import datetime
import sys

print("Welcome to your best and newest Pomodoro app!")
input("Press enter to begin 25 minute work timer: ")

study_times = 0

def work_timer():
    global study_times
    minutes = 0
    print("25 minute timer starts now!")
    while minutes <= 25:
        time.sleep(60)
        minutes = minutes + 1
    print(f"{study_times} study times completed... Time for a break!")

work_timer()

def break_timer():
    global study_times
    