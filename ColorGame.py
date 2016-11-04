import os


### Guess The Color Game ###

def banner():
    # displays banner
    print "\t********************************"
    print "\t******* Color Game 1.0 *********"
    print "\t********************************\n"

def menu():
    # displays menu and waits for user input
    print "[1] Red\n[2] Green\n[3] Blue\n[q] Quit\n"
    return raw_input("\nWhat's your favorite color?\n\n")

CHOICE = ""
os.system('clear')
banner()
while CHOICE != "q":

    CHOICE = menu()

    if CHOICE == "1":
        # win condition
        os.system("clear")
        banner()
        print "Correct!"
        print "You are win!\n"
    elif CHOICE == "2" or CHOICE == "3":
        # lose condition
        os.system("clear")
        banner()
        CHOICE2 = ""
        print "WRONG!"
        print "I am dissapoint\n"
        CHOICE2 = raw_input("Hit enter to try again\nEnter [q] to quit\n")
        if CHOICE2 == "":
            # try again
            os.system('clear')
            banner()
        elif CHOICE2 == "q":
            # quit
            CHOICE = "q"
    elif CHOICE == "q":
        # quit
        os.system("clear")
        banner()
        print "GOODBYE\n"
    else:
        # unknown CHOICE
        os.system("clear")
        banner()
        print "Sorry, I didn't understand that, try again.\n"
        