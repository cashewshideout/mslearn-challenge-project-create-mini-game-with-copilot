# Allow user to input text from three options: rock, paper or scissors
# Computer will randomly select one of the three options
# Determine the winner based on the rules of the game
# Display the winner
# Allow user to play again or exit the game
# Rules are as follows:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

import random

def main():

    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following options: rock, paper, or scissors")

    while True:
        user_choice = input("Enter your choice: ").lower()
        # Check if user input is valid
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"Computer choice: {computer_choice}")

        # Compare computer choice and user choice to determine the winner based on rules

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
            else:
                print("Computer wins!")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
            else:
                print("Computer wins!")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
            else:
                print("Computer wins!")
                
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()



