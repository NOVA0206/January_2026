# ================================
# DAY 03: PYTHON DICTIONARIES
# ================================

student = {
    "name": "Jeevan",
    "age": 22,
    "course": "Computer Science",
    "skills": ["Python", "Logic"]
}

# Access values
print("Name:", student["name"])
print("Skills:", student["skills"])

# Add new key
student["city"] = "Pune"

# Update value
student["age"] = 23

# Loop through dictionary
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)

# Nested dictionary
project = {
    "title": "Anime Tracker",
    "tech": {
        "language": "Python",
        "type": "Console App"
    }
}

print("\nProject Language:", project["tech"]["language"])

# Check key existence
if "city" in student:
    print("\nCity is available in student data")

print("\nDay 03 completed ✅")
