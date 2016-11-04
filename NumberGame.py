import os
import random

### Guess The Color Game ###

# cl.s on windows clea.r on linux

def banner():
    # displays banner
    print "\t********************************"
    print "\t******* Color Game 1.0 *********"
    print "\t********************************\n"

def menu():
    # displays menu and waits for user input
    print "Pick a number, 1, 2, or 3!\n"
    return raw_input("enter [q] to quit\n\n")

def unknown():
    # unknown CHOICE
    os.system("cls")
    banner()
    print "Sorry, I didn't understand that, try again.\n"

NUMBER = str(random.randint(1,3)) # getting ready to change game to random number
# NUMBER = str(NUMBER)
CHOICE = ""
os.system('cls')
banner()
while CHOICE != "q":

    CHOICE = menu()

    if CHOICE == NUMBER:
        # win condition
        os.system("cls")
        banner()
        print "Correct!"
        print "You are win!\n"
    elif CHOICE != NUMBER:
        # lose condition
        os.system("cls")
        banner()
        print "WRONG!"
        print "Try again, \n"
    elif CHOICE == "q":
        # quit
        os.system("cls")
        banner()
        print "GOODBYE\n"
    else:
       unknown()
'''
        CHOICE2 = ""
        CHOICE2 = raw_input("Hit enter to try again\nEnter [q] to quit\n")
        if CHOICE2 == "":
            # try again
            os.system('cls')
            banner()
        elif CHOICE2 == "q":
            # quit
            CHOICE = "q"
        else:
            unknown() 
'''
