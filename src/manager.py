import csv
import os

FILE_NAME = "data/expenses.csv"

def load_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            expenses.append(row)

    return expenses


def save_expense(expense):

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                [
                    "Date",
                    "Category",
                    "Amount",
                    "Description"
                ]
            )

        writer.writerow(expense.to_list())
