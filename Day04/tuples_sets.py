# ================================
# DAY 04: TUPLES & SETS
# ================================

# Tuple (immutable)
languages = ("Python", "Java", "C++")
print("Languages:", languages)
print("First Language:", languages[0])

# Tuple unpacking
lang1, lang2, lang3 = languages
print("Unpacked:", lang1, lang2, lang3)

# Set (unique values)
skills = {"Python", "AI", "Python", "ML"}
print("\nSkills Set:", skills)

# Add & remove
skills.add("DL")
skills.remove("AI")
print("Updated Skills:", skills)

# Set operations
backend = {"Python", "Java"}
ai_stack = {"Python", "ML", "DL"}

print("\nCommon Skills:", backend & ai_stack)
print("All Skills:", backend | ai_stack)

print("\nDay 04 completed ✅")
