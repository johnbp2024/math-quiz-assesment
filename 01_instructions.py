def yes_no(question):
    """checks user response to question is yes or no/y or n then returns yes or no then"""
    while True:
        response = input(question).lower()
        #  #user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


def instructions():
    """prints instructions"""
    print("""
    ***instructions***
    press start and try and get the answers right!
    FILL IN LATER!
    FILL IN LATER!
    FILL IN LATER!
    FILL IN LATER!
    FILL IN LATER!
    """)
print()
print("➕➕➕welcome to the math quiz game➖➖➖")

want_instructions = yes_no("do you want to see the instructions?").lower()
if want_instructions == "yes":
    instructions()
print()
print("program continues")