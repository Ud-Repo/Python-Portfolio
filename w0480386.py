#Create two string variables, str1 and str2, and concatenate them into a third variable result_str.
First_name = "Markovic"
surname = " Keisha"
Full_name = First_name + surname
print(Full_name)

#Given a string sentence, extract and print the first five characters.
subject = "Python"
print (subject[0:5])

#Create a string that includes variables. Use string formatting to insert values into the string.

height = 8
text = "My sister has a big bed. It is {} cm long."
print(text.format(height))



#Using a for loop, print the numbers from 1 to 10.
for s in range(1,11,1) :
    print(s-1)

#Write a function to calculate the factorial of a number using a while loop.
# accept input number from user
n = int(input("Enter any number: "))

# logic to calculate the factorial of a number
f = 1
while n >= 1:
    f *= n
    n -= 1

# print output
print("Factorial is", f)


#Create two sets, set1 and set2, and find and print their intersection.
Set1 = {"Beaver-tail", "Carrots", "Stew"}
Set2 = {"Beans", "Poutine", "Beaver-tail"}
set3 = Set1.intersection(Set2)
print(set3)

#Create a list of numbers. Perform the following operations and print the result:
s = [1,2,3,4,5,6,7,8,9]
z = sum(s)
y = max(s)
w = min(s)
a = sum(s) / len(s)

print(z)
print(y)
print(w)
print(a)


#Generate a list of squares of numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range (1, 11,2)]
print (squares)

#Create a tuple with three values. Unpack the tuple into three variables and print them.
cars = ("Mazda","Lamborghini","Cheverolet")
(luxury , supercar , truck) = cars
print(luxury)
print(supercar)
print(truck)

Student_dict={
     "name" :"Jake",
    "Age" : 33,
    "City": "Connecticut"
}
for keys,values in Student_dict.items():
   print (keys,values)

#Create a nested dictionary representing information about students and their grades. Print the average grade for each student.
#student_scores = {
"Modupe" :{'math': 90,'Agric':60}
"Jill" : {'math': 85,'Agric':80}
"Charlie" : {'math':50, 'Agric':89}
"Uduak" : {94,}
"Teagen" : {80,}
"Mark" : {68,}
"Bihan" : {80,}
"Marcus" :{98,} 
"Davis" :{'math':103,'Agric':79}
"Opadele": {'math' : 98, 'Agric' :76}
#}
# Print the scores
#(print (student_scores)

#find the average
#average = sum(student_scores.values()) / len(student_scores)
#print(f"{student_scores}'s average score : {average}"))

#Write a function that takes two arguments and returns their sum.
def add(a,b) :
    return a+b
print ("The sum of the numbers 4 and 39 is :",add(4,39))

# Python code to
# demonstrate readlines()

L = ["Remove\n", "Sue\n", "Add \n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
	count += 1
	print("Line{}: {}".format(count, line.strip()))
     
     #Write a list of strings to a new text file named 'output.txt'.
list = [1,2,3,4]

filename = ('output.txt')
outfile = open(filename, 'w')
outfile.writelines('list')
outfile.close()

set1 = {1,2,3,4,5}
set2 = {2,3,5,6,7,8}
difference_set = set1 & set2
print(difference_set)

aser = {1,2,3,4,5,6,7,8}
total = 0
for t in aser :
     total += t
     print(total)



#

     my_list = [2, 8, 4, 1, 7]

largest_number = None

for number in my_list:
    if largest_number is None or largest_number < number:
        largest_number = number

# ✅ get the largest number
print(largest_number)  # 👉️ 8

# ✅ get the index of the largest number
print(my_list.index(largest_number))  # 👉️ 1

my_numbers = [1,2,3,4,5,6,7,8,9,]
max = sorted(my_numbers)[-1]
print(max)