# ================================
# LIST OPERATIONS
# ================================

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three elements:", numbers[0:3])
print("Last two elements:", numbers[-2:])

# Add elements
numbers.append(60)
numbers.insert(2, 25)
numbers.extend([70, 80])

print("After adding elements:", numbers)

# Remove elements
numbers.remove(30)
removed_item = numbers.pop()
print("Removed item:", removed_item)
print("After removal:", numbers)

# Copy vs Reference
copy_list = numbers.copy()
numbers.append(90)

print("Original list:", numbers)
print("Copied list:", copy_list)

print("\nList operations completed ✅")
