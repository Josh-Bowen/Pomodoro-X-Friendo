# from time import time
import random

# import time

# active = False

# def pomodoro():
#     while True:
#         try:
#             global active
#             work_start = input("Press enter to begin 25 minute work timer: ")
#             active = True
#             work_timer()
#             active = False
#             break_start = input("Press enter to start break timer")
#             active = True
#             break_timer()
#         except KeyboardInterrupt:
#             exit = input("\nAre you sure you want to exit? (Y / N): ")
#             if exit == "Y":
#                 print(Exception("See Ya!"))
#                 exit()
#             elif exit == "N":
#                 continue

# def commands():
#     if user_input == "work":
#         work_timer()
#     elif user_input == "break":
#         break_timer()
#     elif user_input == "buddy":
#         your_pet()
#         print(pet_mood)
#     elif user_input == "help":
#         help()
#     elif user_input == "bye":
#         exit()


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
    #prints random item from tuple
    print(random.choice(my_tuple))

affirm_tuple()