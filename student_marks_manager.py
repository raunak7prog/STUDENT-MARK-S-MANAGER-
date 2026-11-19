# Student Marks Manager
# Concepts used: input, variables, lists, if-elif-else, while loop, for loop, arithmetic

student_names = []
student_marks = []

print("================================")
print("      STUDENT MARKS MANAGER")
print("================================")

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Show Class Average")
    print("4. Show Topper")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks out of 100: "))

        if marks >= 0 and marks <= 100:
            student_names.append(name)
            student_marks.append(marks)
            print("Student record added successfully!")
        else:
            print("Please enter marks between 0 and 100.")

    elif choice == "2":
        if len(student_names) == 0:
            print("No student records found.")
        else:
            print("\n----- STUDENT RECORDS -----")
            for i in range(len(student_names)):
                print(student_names[i], "-", student_marks[i], "marks")

                if student_marks[i] >= 90:
                    print("Grade: A")
                elif student_marks[i] >= 75:
                    print("Grade: B")
                elif student_marks[i] >= 60:
                    print("Grade: C")
                elif student_marks[i] >= 40:
                    print("Grade: D")
                else:
                    print("Grade: F")

    elif choice == "3":
        if len(student_marks) == 0:
            print("No marks available to calculate average.")
        else:
            total = 0
            for marks in student_marks:
                total = total + marks

            average = total / len(student_marks)
            print("Class Average:", round(average, 2))

    elif choice == "4":
        if len(student_marks) == 0:
            print("No student records found.")
        else:
            highest_marks = student_marks[0]
            topper_index = 0

            for i in range(len(student_marks)):
                if student_marks[i] > highest_marks:
                    highest_marks = student_marks[i]
                    topper_index = i

            print("Class Topper:", student_names[topper_index])
            print("Marks:", highest_marks)

    elif choice == "5":
        print("Thank you for using Student Marks Manager!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
