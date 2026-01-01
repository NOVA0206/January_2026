# ================================
# LISTS ADVANCED - DAY 1
# ================================

print("Python Lists - Real Use")
print("-----------------------")

marks = []

# Taking input
n = int(input("Enter number of subjects: "))

for i in range(n):
    score = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)

print("\nMarks Entered:", marks)

# Calculations
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nResults:")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Sorting
marks.sort()
print("\nSorted Marks (Ascending):", marks)

marks.sort(reverse=True)
print("Sorted Marks (Descending):", marks)

# Searching
search = int(input("\nEnter marks to search: "))
if search in marks:
    print("Marks found in list.")
else:
    print("Marks not found.")

print("\nLists advanced practice completed ✅")
