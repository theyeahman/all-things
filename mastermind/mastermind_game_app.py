from mastermind_code_class import colour_choice, mastermind_code, colour_choices
from mastermind_player_class import  player
import time
import csv

print("\n")
print("Welcome to Mastermind!")
time.sleep(1)
print("Mastermind is a code-breaking game for two players.")
time.sleep(1)
print("However, in this version it will be 1 player vs the computer!")
time.sleep(1)
print("Type 'Help' at any time to get instructions")
time.sleep(1)
print("\n")
time.sleep(1)
print("I will generate a code, which you have to break!")
time.sleep(1)
print("\n")
time.sleep(1)

game_status = "begin"

def pre_game(game_status):
    while game_status != 'start':
        game_status = input("'Start' to begin, 'Help' for help, 'Exit' for exit: \n").lower()

        if game_status == 'help':
            time.sleep(1)
            print("\nVisit the following link for full rules & strategies: https://en.wikipedia.org/wiki/Mastermind_(board_game)#Gameplay_and_rules")
            time.sleep(1)
            print("\nContact yeamanthomas@gmail.com with any issues with the application.\n")
        if game_status == 'exit':
            print("\nThanks for playing! \n")
            exit()
    return game_status

def num_colours_in_game():
    colours = ""
    while not colours:
        try:
            colours = int(input(
    """
How many colours do you want to use as part of the game?
Minimum 2, Maximum 6:  """))
            time.sleep(1)
        except:
            print("Error: Integer only, between 2 and 6")
    return colours

def num_entries_in_code():
    code_entry = ""
    while not code_entry:
        try:
            code_entry = int(input(
        """
And what should the length of the code be?
Minimum 2 Maximum 6:  """))
            time.sleep(1)
        except:
            print("Error: Code length is a whole number > 2")
    return code_entry


def game_start():

    name = input("What's your name? (for high score credit purposes!) ")
    time.sleep(1)
    colours = num_colours_in_game()
    code_length = num_entries_in_code()
    try:
        player_go = player(code_size = code_length, num_col_choice = colours)
    except Exception as err:
        print(err)
        return "start",  "", ""
    time.sleep(1)
    print(
    """

Time to play {}! I have created a secret code, good luck guessing it!
I'll keep track of your score and attempts.
""".format(name))
    time.sleep(2)
    return "long_options", name, player_go

def instructions(name_input):
    print(
        """
{} - it's your turn to add a code.
Here are the colours the computer made their code from.
{}
Remember, the code length is {}
""".format(name_input, colour_choices[:player_details.num_col_choice], player_details.code_size))
    time.sleep(3)
    print("""
If you get the right colour in the right slot, you get 2 points.
If you get the right colour in the wrong slot, you get 1 point.
        """)
    time.sleep(3)


while game_status != "finished":
    if game_status == "begin":
        game_status  = pre_game(game_status)
    elif game_status == "start":
        game_status, name, player_details  = game_start()
    elif game_status == "long_options":
        instructions(name)
        game_status = "short_options"
    elif game_status == "short_options":
        user_go = input("""
'guess' to guess a code, 'view' to view guesses, 'exit' to exit, 'more' for detailed instructions
""").lower()
        if user_go == 'exit':
            game_status = "begin"
        elif user_go == 'more':
            game_status = "long_options"
        elif user_go == 'view':
            print("Your guesses so far")
            guess_list = list(zip(player_details.guesses,player_details.feedback_all))
            for i in guess_list:
                print(i)
        elif user_go == 'guess':
            list_guess = list(map(str.strip,input("Add your guess here, comma seperated:  ").split(",")))
            try:
                player_details.add_guess(code_input = list_guess)
                player_details.check_score()
                time.sleep(2)
                print("""
Good guess, here is your score:
{}""".format(player_details.feedback_all[-1]))
                if player_details.feedback_all[-1] == [2]*player_details.code_size:
                    print("Congratulations! You broke the code!")
                    print("It took you {} attempts".format(player_details.round))
                    time.sleep(2)
                    play_again = input("Play again? Y/N: ").lower()
                    if play_again == "y":
                        game_status = "begin"
                    else:
                        game_status = "finished"
            except ValueError as err:
                time.sleep(1)
                print("something went wrong..")
                print("check the below error message and try again")
                time.sleep(1)
                print(err)
                time.sleep(2)
                user_go == "short_options"


new_score = [name, player_details.round]

with open('scores.csv','r') as scoreboard:
    reader = list(csv.reader(scoreboard, delimiter=','))
    if int(reader[-1][1]) > int(new_score[1]):
        for row in reader[1:]:
            if int(row[1]) > int(new_score[1]):
                new_entry_row = reader.index(row)
                reader.insert(new_entry_row,new_score)
                break
    else:
        reader.append(new_score)
    reader = reader[:5]

print("Latest High Scores!:")
time.sleep(1)
if new_entry_row < 5:
    print("New entry at position {}!!!!".format(new_entry_row))
    time.sleep(1)
for row in reader:
    print(row)

with open('scores.csv', "w") as outfile:
    writer = csv.writer(outfile)
    for line in reader:
        writer.writerow(line)


# Todo
# seperate score boards depending on size of code and number of colours_included
# Log rounds, colours & difficulty in log file, use for statistics on players
# need to imrpvoe view score so its visual plug in based
# need to add pip style guide and check
