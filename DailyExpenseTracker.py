# Initial program message
print("Welcome to the Daily Expense Tracker!")
print()
print(f"""Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

# Initializing Global Variables
con = False
entries = []

# Start while loop
while not con:
    choice = input()

    if choice == "5":
        break
    elif choice == "1":
        entry = float(input())
        entries.append(entry)
        print("Expense added successfully!")
    elif choice == "2":
        if entries == []:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, ent in enumerate (entries):
                print(f"{i+1}. {ent}")
    elif choice == "3":
        total = 0
        if entries == []:
            print("No expenses recorded yet.")
        else:
            for ent in entries:
                total += ent
            print(f"Total expense: {total}")
            avrg = total / len(entries)
            print(f"Average expense: {avrg}")
    elif choice == "4":
        entries.clear()
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")

print("Exiting the Daily Expense Tracker. Goodbye!")
