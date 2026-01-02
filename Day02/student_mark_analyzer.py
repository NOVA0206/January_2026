# ================================
# MINI PROJECT: STUDENT MARKS ANALYZER
# ================================

def get_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    return marks

def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest


def display_report(total, average, highest, lowest):
    print("\n--- Report ---")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


# Main execution
student_marks = get_marks()
total, average, high, low = analyze_marks(student_marks)
display_report(total, average, high, low)

print("\nMini project completed ✅")
