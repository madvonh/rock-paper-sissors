# create a simple rock, paper, scissors game
# provide a welcome message
# get the user's choice
# get the computer's choice
# compare the two choices
# print the results
# ask the user if they want to play again
# say goodbye and end the game
# use one function for the game logic

import random

CHOICES = ["rock", "paper", "scissors"]


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "win"

    return "lose"


def game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Please enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in CHOICES:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(CHOICES)
        print(f"Computer chose: {computer_choice}")

        outcome = determine_winner(user_choice, computer_choice)
        if outcome == "tie":
            print("It's a tie!")
        elif outcome == "win":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    game()