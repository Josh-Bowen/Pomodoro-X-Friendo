# from time import time


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
