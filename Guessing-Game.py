import random

min_number = int(input("Enter the minimum number for the range: "))
max_number = int(input("Enter the maximum number for the range: "))

while max_number < min_number:
    print("Invalid range! The maximum number should be greater than the minimum number.")
    max_number = int(input("Enter the maximum number for the range: "))

secret_number = random.randint(min_number, max_number)

max_guesses = 5
num_guesses = 0

# Start the game
print(f"Choose a number between {min_number} and {max_number}. Can you guess what it?")
while num_guesses < max_guesses:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break

    elif guess < secret_number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")

    num_guesses += 1

if num_guesses == max_guesses:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")
