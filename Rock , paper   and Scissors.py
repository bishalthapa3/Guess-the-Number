# import random

# print("Welcome to Rock, Paper, Scissors!")

# while True:
#     user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     computer_choice = random.choice(["rock", "paper", "scissors"])
    
#     print(f"You chose {user_choice}.")
#     print(f"The computer chose {computer_choice}.")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")

#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != "yes":
#         break


import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print(f"Welcome to Guess the Number! I'm thinking of a number between {lower_limit} and {upper_limit}.")

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            if player_guess < lower_limit or player_guess > upper_limit:
                print(f"Please guess a number between {lower_limit} and {upper_limit}.")
            elif player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"

if __name__ == "__main__":
    while guess_the_number():
        pass

print("Thanks for playing!")

