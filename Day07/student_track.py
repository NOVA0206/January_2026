# =========================================
# STUDENT RECORD MANAGEMENT SYSTEM
# =========================================

FILE = "students_data.txt"

def load_students():
    students = []
    try:
        with open(FILE, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split("|")
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": int(marks)
                })
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE, "w") as file:
        for s in students:
            file.write(f"{s['roll']}|{s['name']}|{s['marks']}\n")


def grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


def add_student(students):
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = int(input("Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })
    save_students(students)
    print("Student added.")


def view_students(students):
    for s in students:
        print(f"{s['roll']} | {s['name']} | {s['marks']} | {grade(s['marks'])}")


def search_student(students):
    roll = input("Enter roll to search: ")
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found.")


def menu():
    print("""
1. Add Student
2. View Students
3. Search Student
4. Exit
""")


def main():
    students = load_students()
    while True:
        menu()
        ch = input("Choice: ")

        if ch == "1":
            add_student(students)
        elif ch == "2":
            view_students(students)
        elif ch == "3":
            search_student(students)
        elif ch == "4":
            break
        else:
            print("Invalid choice")


main()
