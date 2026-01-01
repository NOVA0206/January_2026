# ================================
# CONDITIONS IN PYTHON - DAY 1
# ================================

print("Eligibility & Decision Program")
print("-------------------------------")

age = int(input("Enter your age: "))
education = input("Enter your highest education (jr_college/college): ").lower()
has_passport = input("Do you have a passport? (yes/no): ").lower()

print("\n--- Age Check ---")
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("\n--- Career Readiness Check ---")
if age >= 18 and education == "college":
    print("You are eligible for internships.")
elif age >= 18 and education == "jr_college":
    print("You should focus on skill building.")
else:
    print("Focus on education first.")

print("\n--- Abroad Eligibility Check ---")
if age >= 18:
    if has_passport == "yes":
        print("You are eligible to apply for IELTS and foreign opportunities.")
    else:
        print("Apply for a passport first.")
else:
    print("You are not eligible for abroad opportunities yet.")

print("\nDecision-making using conditions completed ✅")
