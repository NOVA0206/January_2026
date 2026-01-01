# ================================
# PYTHON BASICS - DAY 1
# ================================

print("Welcome to AI Journey 2026")
print("---------------------------")

# Variables
name = "Jeevan"
age = 22
height = 171.5
is_student = True

print("\n--- Basic Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Data types
print("\n--- Data Types ---")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# User input
print("\n--- User Input ---")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_weight = float(input("Enter your weight (kg): "))

print("\n--- User Details ---")
print("Name:", user_name)
print("Age:", user_age)
print("Weight:", user_weight)

# Calculations
print("\n--- Simple Calculations ---")
birth_year = 2025 - user_age
bmi = user_weight / ((height / 100) ** 2)

print("Estimated Birth Year:", birth_year)
print("BMI:", round(bmi, 2))

# String formatting
print("\n--- Formatted Output ---")
print(f"Hello {user_name}, you are {user_age} years old.")
print(f"Your calculated BMI is {round(bmi, 2)}")

print("\nDay 1 Python Basics Completed ✅")
