from sys import exit
import random

choices = ["Rock", "Paper", "Scissors"]

print "\n--------Welcome to Rock-Paper-Scissors--------\n"
print "Get ready... Rock, Paper or Scissors?\n"

player_choice = raw_input("> ")
enemy_choice = random.choice(choices)

print "Computer chose %s" % enemy_choice

if player_choice == "Rock" and enemy_choice == "Rock":
    print "The game is a draw."
elif player_choice == "Rock" and enemy_choice == "Paper":
    print "You win!"
elif player_choice == "Rock" and enemy_choice == "Scissors":
    print "You lose!"
elif player_choice == "Paper" and enemy_choice == "Rock":
    print "You win!"
elif player_choice == "Paper" and enemy_choice == "Paper":
    print "The game is a draw."
elif player_choice == "Paper" and enemy_choice == "Scissors":
    print "You lose!"
elif player_choice == "Scissors" and enemy_choice == "Rock":
    print "You lose!"
elif player_choice == "Scissors" and enemy_choice == "Paper":
    print "You win!"
elif player_choice == "Scissors" and enemy_choice == "Scissors":
    print "The game is a draw."
else:
    print "You need to type in your choice exactly."
