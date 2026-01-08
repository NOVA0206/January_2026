# =========================================
# EXPENSE TRACKER SYSTEM
# =========================================

FILE = "expenses.txt"

def load_expenses():
    expenses = []
    try:
        with open(FILE, "r") as file:
            for line in file:
                date, category, amount = line.strip().split("|")
                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": float(amount)
                })
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    with open(FILE, "w") as file:
        for e in expenses:
            file.write(f"{e['date']}|{e['category']}|{e['amount']}\n")


def add_expense(expenses):
    date = input("Date: ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    total = 0
    for e in expenses:
        print(e)
        total += e["amount"]
    print("Total Spent:", total)


def menu():
    print("""
1. Add Expense
2. View Expenses
3. Exit
""")


def main():
    expenses = load_expenses()
    while True:
        menu()
        ch = input("Choice: ")

        if ch == "1":
            add_expense(expenses)
        elif ch == "2":
            view_expenses(expenses)
        elif ch == "3":
            break
        else:
            print("Invalid choice")


main()
