# ================================
# MENU-BASED FUNCTION PROGRAM
# ================================

def show_menu():
    print("\nChoose an option:")
    print("1. Add numbers")
    print("2. Square a number")
    print("3. Check even or odd")
    print("4. Exit")

def add_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a + b)

def square_number():
    n = int(input("Enter number: "))
    print("Square:", n * n)

def check_even_odd():
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_numbers()
    elif choice == "2":
        square_number()
    elif choice == "3":
        check_even_odd()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")

print("Menu-based program completed ✅")
