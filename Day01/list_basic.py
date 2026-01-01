# ================================
# LISTS BASICS - DAY 1
# ================================

print("Python Lists - Basics")
print("----------------------")

# Creating lists
students = ["Amit", "Rahul", "Sneha", "Priya"]
marks = [78, 85, 90, 67]

print("\nInitial Lists:")
print("Students:", students)
print("Marks:", marks)

# Accessing elements
print("\nAccessing Elements:")
print("First student:", students[0])
print("Last student:", students[-1])

# Updating list values
print("\nUpdating Values:")
students[1] = "Rohan"
marks[3] = 72
print("Updated Students:", students)
print("Updated Marks:", marks)

# Adding elements
print("\nAdding Elements:")
students.append("Neha")
marks.append(88)
print("After Append:", students)

students.insert(2, "Kunal")
print("After Insert:", students)

# Removing elements
print("\nRemoving Elements:")
students.remove("Amit")
removed_mark = marks.pop(0)

print("Students after removal:", students)
print("Removed mark:", removed_mark)

# Looping through list
print("\nLooping through Students:")
for student in students:
    print(student)

print("\nLists basics completed ✅")
