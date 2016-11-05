import os
import random

### Guess The Number Game ###

#cl.s on windows clea.r on linux

def banner():
    #displays banner
    print "\t********************************"
    print "\t********* Number Game **********"
    print "\t********************************\n"

def menu():
    #displays menu and waits for user input
    print "Pick a number, 1 through 10!\n"
    return raw_input("enter [q] to quit\n\n")

def unknown():
    #unknown CHOICE
    os.system("cls")
    banner()
    print "Sorry, I didn't understand that, try again.\n"

NUMBER = str(random.randint(1,10)) #get a random number and turn it into a string to match user input
CHOICE = ""
os.system('cls')
banner()
while CHOICE != "q":

    CHOICE = menu()

    if CHOICE == NUMBER:
        #win condition
        os.system("cls")
        banner()
        print "Correct!"
        print "You are win!\n"
        CHOICE2 = "" 
        #finish replay mechanic
    elif CHOICE != NUMBER and CHOICE != "q":
        #lose condition
        os.system("cls")
        banner()
        print "WRONG!"
        print "Try again. \n"
    elif CHOICE == "q":
        #quit
        os.system("cls")
        banner()
        print "Thanks for playing!\n"
    else:
        unknown()
