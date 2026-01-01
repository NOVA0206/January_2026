# ===================================
# FUNCTIONS WITH LISTS - DAY 1
# ===================================

print("Functions with Lists")
print("---------------------")

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_highest(numbers):
    return max(numbers)

def find_lowest(numbers):
    return min(numbers)

def display_results(numbers):
    print("\nNumbers:", numbers)
    print("Average:", calculate_average(numbers))
    print("Highest:", find_highest(numbers))
    print("Lowest:", find_lowest(numbers))

# Main program
data = []
count = int(input("How many values do you want to enter? "))

for i in range(count):
    value = int(input(f"Enter value {i + 1}: "))
    data.append(value)

display_results(data)

print("\nLists + Functions practice completed ✅")
