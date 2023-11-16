
# step 1 : Create a list of programming languages and difficulty levels
programming_languages = ["Python","Javascript","C++","Ruby","Java"]
Difficulty = [2,3,4,2,5]

#step 2 : combine the two lists. This is called a tuple

quiz_data = list(zip(programming_languages, Difficulty))

print(quiz_data)