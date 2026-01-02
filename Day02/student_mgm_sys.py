students = []   
marks_list = [] 

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Must be between 0 and 100.")
        return

    students.append(name)
    marks_list.append(marks)
    print("Student added successfully!")


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def display_all_students():
    if len(students) == 0:
        print("No student records available.")
        return

    print("\n--- Student Records ---")
    for i in range(len(students)):
        grade = calculate_grade(marks_list[i])
        status = "Pass" if marks_list[i] >= 40 else "Fail"

        print(f"""
Student Name : {students[i]}
Marks        : {marks_list[i]}
Grade        : {grade}
Status       : {status}
--------------------------
        """)


def class_statistics():
    if len(marks_list) == 0:
        print("No data to analyze.")
        return

    total = sum(marks_list)
    average = total / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)

    print("\n--- Class Statistics ---")
    print("Total Students :", len(marks_list))
    print("Average Marks  :", average)
    print("Highest Marks  :", highest)
    print("Lowest Marks   :", lowest)


def show_menu():
    print("""
========= MENU =========
1. Add Student
2. View All Students
3. View Class Statistics
4. Exit
========================
    """)


# -------- MAIN LOOP --------

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        class_statistics()
    elif choice == "4":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
