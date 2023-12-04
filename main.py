import random

# Function to get the choice from the user
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Choose rock, paper, or scissors: ").lower()
    while user_input not in choices:
        print("Invalid choice. Choose again.")
        user_input = input("Choose rock, paper, or scissors: ").lower()
    return user_input

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Main game function
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Let's play the game!
play_game()
