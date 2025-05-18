import random
import sys
from lib2to3.btm_utils import reduce_tree

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def start():
    return render_template('start.html')

def results():
    return render_template('results.html')


def get_user_choice():
    print("Enter your choice: rock, paper, or scissors.")
    user_choice = input("> ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Sorry, no can do! Please choose either rock, paper or scissors.")
        return get_user_choice()
    else:
        return user_choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    winner_message = "You win!"
    loser_message = "Sorry, you lose!"
    tie_message = "It's a tie!"

    if user_choice == computer_choice:
        return tie_message
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return winner_message
    else:
        return loser_message


def main():
    playing = True

    while playing:
        print("Let's play rock, paper, scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You choose: {user_choice}")
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Want a rematch? y/n")
        rematch = input("> ").lower()
        if rematch == "y" or rematch == "yes":
            pass
        elif rematch == "n" or rematch == "no":
            print("Thanks for playing!")
        else:
            print("I'll take that as a no. Thanks fo playing!.")
            playing = False
            sys.exit()

if __name__ == "__main__":
    app.run()