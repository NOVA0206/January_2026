# ================================
# DAY 06: EXCEPTION HANDLING
# ================================

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid integers")

finally:
    print("Program executed safely")

print("\nDay 06 completed ✅")
