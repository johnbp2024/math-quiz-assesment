import random


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


def int_check(question, low=None, high=None, exit_code=None):
    """Checks users enter an integer (optional exit code and high / low values)"""
    # if any integer is allowed
    if low is None and high is None:
        error = "please enter an integer"
    # if the number needs to be more than an integer
    elif low is not None and high is None:
        error = f"please enter a enter a number that is more than or equal to {low}"

    # if the number needs to be between low and high
    else:
        error = f"please enter a number that is between {low} and {high} (inclusive)"

    # error = "please enter an integer"
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

            return response
        except ValueError:
            print(error)


# game variables

rounds_won = 0

rounds_lost = 0

low_num = 0

high_num = 10

operation_list = ["+", "-", "*"]

rounds_played = 0

round_history = ""

correct_or_not = ""

game_history= []

#checking if they want default settings
default_game = yes_no("do you want default game settings? (10 rounds)")
if default_game == "yes":
    max_rounds = 10
#asking how many rounds they want
else:
    max_rounds = int_check("enter the amount of questions you want up to 20", low=1, high=20)

# main game loop

while rounds_played + 1  < max_rounds:
    random_operation = random.choice(operation_list)
    first_num = random.randint(low_num, high_num)
    rounds_played = rounds_lost + rounds_won
    second_num = random.randint(low_num, high_num)

    print(f"{first_num} {random_operation} {second_num}")
    answer = eval(f"{first_num} {random_operation} {second_num}")
    player_input = int_check("what do you think the answer is?")
    if player_input == answer:
        rounds_won += 1
        print("correct answer!")
        correct_or_not = "correct"

    else:
        print("wrong answer, sorry")
        rounds_lost += 1
        correct_or_not = "incorrect"
    round_history =(f"round: {rounds_played + 1}. {first_num} {random_operation} {second_num} = {answer} "
                       f"you got it {correct_or_not}")
    game_history.append(round_history)



#asking if they want to see history
history = yes_no("do you want to see game history?")
if history == "yes":
    print(f"you won:{rounds_won} out of {rounds_played + 1} rounds")
    print(game_history)




