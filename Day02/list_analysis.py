# ================================
# LIST ANALYSIS
# ================================

marks = [78, 85, 92, 67, 88, 74]

print("Marks:", marks)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

# Manual calculation (important concept)
manual_sum = 0
for mark in marks:
    manual_sum += mark

manual_avg = manual_sum / len(marks)

print("Manual Average:", manual_avg)

print("\nList analysis completed ✅")

print("Manual sum matches built-in sum:", manual_sum == total)

# ================================

marks_man = []

print("Manual Entries of Marks:")
subjects = int(input("Enter Number of subjects: "))
print("Enter marks one by one:")
for n in range(subjects):
    mark = int(input(f"Mark for subject {n+1}: "))
    marks_man.append(mark)

print("Marks entered by the user:", marks_man)
