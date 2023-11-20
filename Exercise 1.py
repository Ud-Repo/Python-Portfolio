import random

# Create two separate lists
programming_languages = ['Python', 'JavaScript', 'C++', 'Ruby', 'Java']
difficulty_levels = [2, 3, 4, 2, 5]

# Combine the two lists into a list of tuples (quiz)
quiz = list(zip(programming_languages, difficulty_levels))

# Shuffle the quiz for a random order
random.shuffle(quiz)

# Initialize player's score
score = 0

# Loop through the quiz
for language, difficulty in quiz:
    print(f"What is the difficulty level of '{language}'?")
    guess = int(input("Enter your guess (1-5): "))
    
    # Check if the guess is correct
    if guess == difficulty:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The difficulty level of '{language}' is {difficulty}.")
    print()  # Empty line for readability

# Display final score
print(f"Quiz ended. Your final score is: {score}/{len(quiz)}")
