import csv
import os

file_name = "expenses.csv"

def setup_file():
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
        print("File created!")
    else:
        print("File already exists.")

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Rent/Other): ")
    description = input("Enter description: ")

    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!")

def view_monthly():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        print(f"\n--- Expenses for {month}-{year} ---")
        total = 0

        for row in reader:
            if f"-{month}-{year}" in row[0] or f"/{month}/{year}" in row[0]:
                print(f"Date: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]} | Desc: {row[3]}")
                total += float(row[1])

    print(f"\nTotal: ₹{total}")

def view_yearly():
    year = input("Enter year (YYYY): ")
    monthly_totals = {}

    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if year in row[0]:
                if "-" in row[0]:
                    month = row[0].split("-")[1]
                elif "/" in row[0]:
                    month = row[0].split("/")[1]

                if month not in monthly_totals:
                    monthly_totals[month] = 0
                monthly_totals[month] += float(row[1])

    print(f"\n--- Yearly Summary for {year} ---")
    grand_total = 0
    for month, total in sorted(monthly_totals.items()):
        print(f"Month {month}: ₹{total}")
        grand_total += total
    print(f"\nGrand Total: ₹{grand_total}")

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Monthly Expenses")
        print("3. View Yearly Summary")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_monthly()
        elif choice == "3":
            view_yearly()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

setup_file()
menu()