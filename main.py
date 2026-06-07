from src.expense import Expense
from src.file_manager import save_expense, load_expenses
from src.reports import total_expense, category_summary
from src.menu import display_menu
from src.utils import validate_amount, validate_date

import shutil


def add_expense():

    print("\n===== ADD NEW EXPENSE =====")

    amount = input("Enter Amount: ")

    if not validate_amount(amount):
        print("❌ Invalid Amount")
        return

    category = input("Enter Category: ")

    date = input("Enter Date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("❌ Invalid Date Format")
        return

    description = input("Enter Description: ")

    expense = Expense(
        amount,
        category,
        date,
        description
    )

    save_expense(expense)

    print("\n✅ Expense Added Successfully!")


def view_expenses():

    expenses = load_expenses()

    print("\n===== ALL EXPENSES =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense)


def show_total():

    expenses = load_expenses()

    total = total_expense(expenses)

    print(f"\n💰 Total Expense: ₹{total:.2f}")


def show_category_summary():

    expenses = load_expenses()

    summary = category_summary(expenses)

    print("\n===== CATEGORY SUMMARY =====")

    if len(summary) == 0:
        print("No expense data available.")
        return

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def backup_data():

    try:

        shutil.copy(
            "data/expenses.csv",
            "data/backup_expenses.csv"
        )

        print("\n✅ Backup Created Successfully!")

    except Exception as e:

        print(f"\n❌ Backup Failed: {e}")


def main():

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (1-6): "
        )

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_category_summary()

        elif choice == "4":
            show_total()

        elif choice == "5":
            backup_data()

        elif choice == "6":

            print(
                "\nThank you for using Personal Finance Manager!"
            )

            break

        else:

            print(
                "\n❌ Invalid Choice. Please try again."
            )


if __name__ == "__main__":
    main()
