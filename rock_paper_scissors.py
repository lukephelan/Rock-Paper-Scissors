"""Game of Rock-Paper-Scissors that keeps a running tally of outcomes.
"""

# Importation of relevant modules.
# Allow for safe exit from program, randomising the computer's weapon choice, and pausing between display text.
from sys import exit
import random
from time import sleep

# Introductory text.
print "\n--------Welcome to Rock-Paper-Scissors--------"
sleep(1)

# Sets game outcome results to 0.
no_of_games = 0
win_count = {'player': 0, 'enemy': 0, 'draw': 0}

def option_screen():

    print "\nPlease select an option:"
    print "\n\t1 - Play a game"
    print "\t2 - Exit"
    
    # Utilising the try statement to prevent EOFError when user presses ctrl-d within raw_input.
    try:        
        option = raw_input("> ") 
        # Allows for multiple input options from the user.
        if option in {"1", "Play a game", "play a game", "1 - Play a game", "1 - play a game", "play", "Play"}:
            play_rps()
        elif option in {"2", "Exit", "exit", "2 - Exit", "2 - exit", "quit", "Quit", "e", "E"}:
            print "Bye!"
            exit(0)
        else:
            print "Sorry, that doesn't make any sense."
            option_screen()

    except EOFError:
        exit(0)

def play_rps():

    weapons = {"Rock": 1, "Paper": 2, "Scissors": 3}
    # Global variables to keep track of the games.
    global no_of_games
    global win_count
    
    print "\nGet ready... Rock, Paper or Scissors?\n"

    # Utilising the try statement to prevent EOFError when use presses ctrl-d within raw_input.
    while True:
            try:
                player_choice = raw_input("> ")
                if player_choice not in weapons:
                    print "Sorry, that doesn't make any sense to me. Try again."
                    print "Rock, Paper or Scissors?\n"
                    continue
                else:
                    break   
            except EOFError:
                exit(0)
    
    # Computer chooses a random weapon from the weapons dictionary.        
    enemy_choice = random.choice(weapons.keys())

    player_wins = "You win!"
    enemy_wins = "You lose!"
    draw = "It's a draw."

    print "The computer chose %s.\n" % enemy_choice
    sleep(0.5)

    # Mathematical equation to determine who wins the game.
    outcome = weapons[player_choice] - weapons[enemy_choice]

    # All outcome combinations and their result.
    if outcome in {-2, 1}:
        print player_wins
        sleep(1)
        no_of_games += 1
        win_count['player'] += 1
        print  "Out of %d games, you have won %d times, lost %d times and drawn %d times." % (no_of_games, 
                                win_count['player'], win_count['enemy'], win_count['draw'])
        option_screen()
    elif outcome in {-1, 2}:
        print enemy_wins
        sleep(1)
        no_of_games += 1
        win_count['enemy'] += 1
        print  "Out of %d games, you have won %d times, lost %d times and drawn %d times." % (no_of_games, 
                                win_count['player'], win_count['enemy'], win_count['draw'])
        option_screen()
    elif outcome == 0:
        print draw
        sleep(1)
        no_of_games += 1
        win_count['draw'] += 1
        print  "Out of %d games, you have won %d times, lost %d times and drawn %d times." % (no_of_games, 
                                win_count['player'], win_count['enemy'], win_count['draw'])
        option_screen()
    else:
        option_screen()

option_screen()