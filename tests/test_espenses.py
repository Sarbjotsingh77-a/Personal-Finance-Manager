from src.expense import Expense

expense = Expense(
    500,
    "Food",
    "2024-01-01",
    "Lunch"
)

print(expense)

assert expense.amount == 500.0
assert expense.category == "Food"

print("Test Passed Successfully!")
