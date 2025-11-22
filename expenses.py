expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, shopping, etc): ")
    note = input("Enter a short note: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note
    })

    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")
        total += exp["amount"]

    print(f"\nTotal Spending: ₹{total}\n")

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()