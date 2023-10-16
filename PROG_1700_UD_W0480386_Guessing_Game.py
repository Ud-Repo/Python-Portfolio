import random

def play_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        user_guess = input("Guess the number between 1 and 10: ")
        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

    if attempts == max_attempts and user_guess != number_to_guess:
        print(f"Sorry, you've reached the maximum of {max_attempts} attempts. The number was {number_to_guess}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_guessing_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_guessing_game()
