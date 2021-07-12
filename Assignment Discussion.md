Assignment Discussion

So the terminal assessment piece is out now, and there's a lot to take in when it comes to the requirements there. 

Here's a bit of a breakdown.  This writeup isn't a replacement for the submission requirements, so once you're done reading here, go look at the submission requirements on canvas! Don't forget to read the marking rubric too!

You need to submit:

    A software development plan

    An implementation plan

    A production log with 2 status updates (these are submitted before the due date)

    Screenshots/an export of you using a project management tool like Trello

    The application itself

    2x feature tests

    One or more bash scripts.

In addition to this, there are some guidelines on how you should go about producing the work:

    You need to use git/github, with at least 20 commits. 

This sounds like a lot, right? But don't worry! Most of this is stuff you would have to do anyway in order to write the app. So the good news is, if you get to work on putting together the peripheral submission elements, by the time you get to the point of starting to write code, you should find that most of the hard work is already out of the way.

Let's break those submission requirements down a bit...

The software development plan

This is a document communicating how you plan to create your app. We've broken down what you need to include in the submission requirements, so have a read there. Briefly, it's:

    A statement of purpose and scope for your app. 

    A list of at least three features your app will have.

    An outline of the intended user experience/interaction for the features of your app

    A control flow diagram (flowchart) showing how the logic of your app is structured

There are some important specifications for what you need to include in each of these, so go read the submission requirements!  

The implementation plan

This should be in the form of a table in a .md document. You need to include each of the features with:

    An outline of how the feature will be implemented (a function? a module? very broadly, how will the implementation deliver the feature?)

    a checklist of tasks describing the process you'll follow to develop each feature (at least 5 tasks per feature)

    A priority for each feature and each checklist item

    A deadline for each feature and checklist item

The production log

This is a pair of status updates, together in a .md file.  Add a status update when you hit a crucial point in your development process, and then send me your updated file to report on how you're going! You'll also need to include the production log in your submitted .zip. 

    Status updates just need to be 100-200 words, and describe where you're up to, what you're working on, what challenges you've encountered, what solutions you've created. The idea is that these are a professional document, so don't write too informally, but don't waste time trying to craft a perfect essay.  Try to get one out by Monday, and one out around Thursday next week.

Screenshots/an export of you using a project management tool

I recommend using Trello, it's great. You should actually use it to plan your process - don't just slap together some screenshots after you're finished. It takes minutes to set up, and will help you organise yourself. Take the checklists that you created for the implementation plan, turn each item into a Trello card, and progress them as you complete them.

The application itself

    You need to employ command line arguments (we'll discuss those tomorrow), so don't worry about them for now

    you need to take input somehow. You can do this using the input() function, or reading from a file, or both

    You need to generate output. You can do this using print(), or writing to a file, or both.

    You must utilise a range of programming concepts and structures using Python 3 such as

        variables and variable scope

        loops and conditional control structures

        error handling

    Remember to use comments to explain the more complex parts of your code and point out the purpose of functions. They don't have to be long, just enough to make your intentions clear. This will help us with marking and make it easier to give you a good grade.

The feature tests 

Each test should focus on a feature of your app, specifying the expected behaviour of the program throughout the test scenario. Each test needs at least two use scenarios of the feature (one correct and one incorrect use is often a good pattern). 

For each feature test:

    state what feature is being tested

    state each of the scenarios in turn with

        any inputs

        the expected output

        the actual output

        whether this is a success or a fail (if your program fails at first, this is a good time to write a status update for your log! Then add a task to your trello board to fix the bug, with a deadline. Then fix the bug and run the test again!)

Write this up in a .md document and submit it with everything else.


    Design a help file which includes a set of instructions which accurately describe how to use and install the application.

    You must include:
    - steps to install the application
    - any dependencies required by the application to operate
    - any system/hardware requirements
    - a written explanation of the different features of the application

    The help file should be 100 - 200 words.
 

The bash script/s

We'll be discussing these in class later this week. Don't stress about them yet. Once we've covered them, here's the deal:

Priority 1 - write an executable bash script that will run your app from the command line.

Priority 2 - get it to accept arguments (one is fine, more than one is fine too). Have it print an error if unacceptable arguments are supplied. 

Priority 3 - See if you can get your script to check that the environment is suitable for running your app. Is python installed? If your app requires third party modules, are they installed? Have it fail gracefully and print error messages if necessary. 

Priority 4 - If you're feeling really super on top of things, see if you can write another script to automate your test cases. Get everything else done first - this is your last priority.