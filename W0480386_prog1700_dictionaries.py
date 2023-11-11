student_scores = {
"Modupe" : 90,
"Jill" : 85,
"Charlie" : 50,
"Uduak" : 94,
"Teagen" : 80,
"Mark" : 68,
"Bihan" : 80,
"Marcus" :98,
"Davis" :103,
"Opadele": 98
}
# Print the scores
print (student_scores)

#find the average
average = sum(student_scores.values()) / len(student_scores)
print(f"Average = {average}")

  #calculate highscorer
highest_score = max(student_scores.values())
top_student = [name for name, score in student_scores.items() if score == highest_score]

print(f"Highest Score: {highest_score}")
print(f"Student(s) with the highest score: {', '.join(top_student)}")
#look up a student's score
student_name = input("Enter a student's name: ")

if student_name in student_scores :
    print(f"{student_name}'s score is: {student_scores[student_name]}")
else:
    # Print Message if Student is Not Found
      print(f"Student '{student_name}' not found.")
      
     #Edit a student's score
      student_name = input("Enter the student's name whose score you want to update: ")
if student_name in student_scores:
     new_score = int(input(f" {student_name}'s new score: "))
else:
     print(f"Student '{student_name}' not found.")

   