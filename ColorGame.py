import os


### Guess The Color game ###

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
        os.system("clear")
        banner()
        print "Correct!"
        print "You are win!\n"
    elif CHOICE == "2" or CHOICE == "3":
        os.system("clear")
        banner()
        choice2 = ""
        print "WRONG!"
        print "I am dissapoint\n"
        choice2 = raw_input("Hit enter to try again\nEnter [q] to quit\n")
        if choice2 == "":
            os.system('clear')
        elif choice2 == "q":
            CHOICE = "q"
    elif CHOICE == "q":
        os.system("clear")
        banner()
        print "GOODBYE\n"
    else:
        os.system("clear")
        banner()
        print "Sorry, I didn't understand that, try again.\n"
        