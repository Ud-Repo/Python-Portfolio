# Student records list to store dictionaries of student information
student_records = []

# Menu options function
def display_menu():
    print("Student Record Management")
    print("1. Create a new student record")
    print("2. Read all student records")
    print("3. Update a student record")
    print("4. Delete a student record")
    print("5. Exit")

# Main loop for the program
while True:
    display_menu()  # Display the menu options
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # Create a new student record
        student_id = len(student_records) + 1
        student_name = input("Enter student name: ")
        grade = input("Enter grade: ")

        # Create a dictionary for the new student record
        student_record = {
            "Student ID": student_id,
            "Student Name": student_name,
            "Grade": grade
        }

        # Add the student record to the list
        student_records.append(student_record)
        print("Student record created successfully!\n")

    elif choice == '2':
        # Read all student records
        if not student_records:
            print("No student records available.\n")
        else:
            for record in student_records:
                print(record)
            print()

    elif choice == '3':
        # Update a student record
        if not student_records:
            print("No student records available to update.\n")
        else:
            student_id = int(input("Enter student ID to update: "))
            for record in student_records:
                if record["Student ID"] == student_id:
                    record["Student Name"] = input("Enter new student name: ")
                    record["Grade"] = input("Enter new grade: ")
                    print("Student record updated successfully!\n")
                    break
            else:
                print("Student ID not found.\n")

    elif choice == '4':
        # Delete a student record
        if not student_records:
            print("No student records available to delete.\n")
        else:
            student_id = int(input("Enter student ID to delete: "))
            for record in student_records:
                if record["Student ID"] == student_id:
                    student_records.remove(record)
                    print("Student record deleted successfully!\n")
                    break
            else:
                print("Student ID not found.\n")

    elif choice == '5':
        # Exit the program
        print("Exiting the Student Record Management program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
