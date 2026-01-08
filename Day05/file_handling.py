# ================================
# DAY 05: FILE HANDLING
# ================================

filename = "daily_log.txt"

# Write file
with open(filename, "w") as file:
    file.write("Day 05: File handling practice\n")

# Append file
with open(filename, "a") as file:
    file.write("Learning persistence in Python\n")

# Read file
print("\nFile Content:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

print("\nDay 05 completed ✅")
