import os

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.


### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")
    
def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")
    
    return raw_input("What would you like to do? ")
    

### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        print("\nHere are the people I know.\n")
    elif choice == '2':
        print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")