# Software Development Plan


## Purpose & Scope
The purpose of this app is to allow the user to have a pomodoro style timer that runs in the terminal, with an added layer of motivation to get their work done. 

The app has the ability to run a 25 minute timer, for the user to time themselves as they work or study. They can also run a break timer, that runs for 5 minutes or 15 minutes if four work timers have run. 
The extra motivation comes in the form of a Tamagotchi style pet that has different moods depending on how much the user sticks to the pomodoro timers or if they ignore it. 
For a student like myself, pomodoro timers are a great way to promote productivity. 

    
## Interaction and Experience
When the app is started, there will be a welcome message and brief explanation on what the app is, as well as how to use it. 
The user will be prompted to run a command to start the timer.  


## Functions
1) Timers<br>
A timer that counts down from 25 Minutes.
* Requires prompt and user input to begin
* Counter will count down from 25 minutes
* Update the user with time remaining
* Requires sound and/ or visual indication when finished 
* If the user inputs the wrong prompt, an error message will be displayed and the list of accaptable inputs will be displayed. 

<br>

2) Friendo <br>
"Tamagotchi" style pet(Avatar) 
* Meter that represents "Happiness" of avatar
* goes down when the user doesnt start the break timer after the work timer(requires prompt)
* goes up when user break timer and work timer runs. 
* If the meter is high, a happy emoji will be displayed
* If the meter is half-way a neutral expression emoji will display
* when the meter is low, a sad emoji will display
* User can check how their "pet" is at any time. 

<br>

3) User Interface <br>
Allows the user to ineract with different functions of the app
* By entering the correct command the user can:
    * Exit the app 
    * Check happiness of Friendo
    * Start work/ study timer
    * Start break timer
    * Ask for an affirmation
    * Clear the terminal window
    * Print the list of accepted commands

## User Interaction and Experience
On launch of the app, the user will be greated with a brief explanation of what the app is and how it works, as well as being prompted to name their pet. After which the app will launch into its main feature, in which the user can enter one of several commands. The application will display a list of the commands that can be used. 
To use the other features of the app, the user needs to input the appropriate command, such as "work" or "break" to start one fo the timers or "bye" to quit the application. 
if the user inputs the wrong command, the user is told that the command is wrong, that they can type "help" for a list appropriate commands. If the user presses control + C to exit, they will be met with a farewell message and the app will exit. 

## Control Flow Diagram 


* Testing
* Deployment




## Features

## Control Flow Diagram

