import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
number_to_guess = 2
max_attempts = 10
attempts = 1
game_run = True
guess_run = True
while game_run:
    while guess_run:
        try:
            guess = int(input("Enter your guess: "))
            guess_run = False
        except:  
            guess_run = True
    if guess == number_to_guess:
        print("Congratulations! You've guessed the number!")
        game_run = False
    elif attempts >= max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        game_run = False
    elif guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    attempts += 1
    continue
print("Game Over. Thanks for playing!")