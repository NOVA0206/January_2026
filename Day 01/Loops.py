# ================================
# LOOPS IN PYTHON - DAY 1
# ================================

print("Python Loops Practice")
print("----------------------")

# FOR LOOP
print("\n--- For Loop Example ---")
for day in range(1, 8):
    print("Day", day, ": Practice Python and AI")

# FOR LOOP WITH CALCULATION
print("\n--- Marks Calculation ---")
total_marks = 0

for subject in range(1, 6):
    marks = int(input(f"Enter marks for subject {subject}: "))
    total_marks += marks

average = total_marks / 5
print("Total Marks:", total_marks)
print("Average Marks:", average)

# WHILE LOOP
print("\n--- While Loop Example ---")
count = 1
while count <= 5:
    print("Attempt", count, ": Stay consistent")
    count += 1

# MENU-BASED LOOP
print("\n--- Simple Menu Program ---")
choice = ""

while choice != "exit":
    print("\nChoose an option:")
    print("1. Say Hello")
    print("2. Motivation Message")
    print("Type 'exit' to quit")

    choice = input("Enter choice: ").lower()

    if choice == "1":
        print("Hello! Welcome to AI Journey 2026 🚀")
    elif choice == "2":
        print("Consistency today creates success tomorrow.")
    elif choice == "exit":
        print("Exiting program...")
    else:
        print("Invalid choice. Try again.")

print("\nLoops practice completed ✅")
