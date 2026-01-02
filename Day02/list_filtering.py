# ================================
# LIST FILTERING
# ================================

scores = [45, 78, 88, 32, 90, 67, 55]

passed = []
failed = []

for score in scores:
    if score >= 50:
        passed.append(score)
    else:
        failed.append(score)

print("All Scores:", scores)
print("Passed:", passed)
print("Failed:", failed)

# Filter using condition
high_scores = [score for score in scores if score >= 80]

print("High Scores (80+):", high_scores)

print("\nList filtering completed ✅")
