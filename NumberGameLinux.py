import os
import random

### Guess The Color Game ###

# linux version

def banner():
    # displays banner
    print "\t**********************************"
    print "\t******** !Number Game! ***********"
    print "\t**********************************\n"

def menu():
    # displays menu and waits for user input
    print "Pick a number, 1 through 10!\n"
    return raw_input("enter [q] to quit\n\n")

def unknown():
    # unknown CHOICE
    os.system("clear")
    banner()
    print "Sorry, I didn't understand that, try again.\n"

NUMBER = str(random.randint(1,10)) # getting ready to change game to random number
CHOICE = ""
os.system('clear')
banner()
while CHOICE != "q":

    CHOICE = menu()

    if CHOICE == NUMBER:
        # win condition
        os.system("clear")
        banner()
        print "Correct!"
        print "You are win!\n"
        CHOICE2 = "" 
        # finish replay mechanic
    elif CHOICE != NUMBER and CHOICE != "q":
        # lose condition
        os.system("clear")
        banner()
        print "WRONG!"
        print "Try again. \n"
    elif CHOICE == "q":
        # quit
        os.system("clear")
        banner()
        print "Thanks for playing!\n"
    else:
        unknown()
