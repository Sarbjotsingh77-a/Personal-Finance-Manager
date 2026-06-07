def total_expense(expenses):

    total = sum(
        float(exp[2])
        for exp in expenses
    )

    return total


def category_summary(expenses):

    summary = {}

    for exp in expenses:

        category = exp[1]
        amount = float(exp[2])

        summary[category] = (
            summary.get(category, 0)
            + amount
        )

    return summary
