2nd code 

# number_guessing_game.py

import random

def save_result(name, attempts):
    with open("guess_log.txt", "a") as file:
        file.write(f"{name} guessed the number in {attempts} attempts.\n")

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range 1–100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations, {name}! You guessed the number in {attempts} attempts.")
                save_result(name, attempts)
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

# ✅ Corrected entry point
if _name_ == "_main_":
    number_guessing_game()