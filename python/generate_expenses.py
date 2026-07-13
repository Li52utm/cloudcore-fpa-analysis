import pandas as pd
import random
from pathlib import Path

random.seed(42)

# Departments
departments = [1, 2, 3, 4, 5]

expense_types = {
    "Salary": (5000, 15000),
    "Marketing": (1000, 8000),
    "Cloud Hosting": (300, 5000),
    "Software": (100, 3000),
    "Travel": (200, 4000),
    "Office": (100, 1500)
}

months = pd.date_range(
    start="2024-01-01",
    end="2026-04-01",
    freq="D"
)

expenses = []

expense_id = 1

for day in months:

    transactions = random.randint(5, 15)

    for _ in range(transactions):

        expense = random.choice(list(expense_types.keys()))

        low, high = expense_types[expense]

        expenses.append({

            "expense_id": expense_id,

            "expense_date": day.date(),

            "department_id": random.choice(departments),

            "expense_type": expense,

            "amount": round(random.uniform(low, high),2)

        })

        expense_id += 1

expenses_df = pd.DataFrame(expenses)

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

expenses_df.to_csv(
    output_folder / "expenses.csv",
    index=False
)

print(f"Generated {len(expenses_df)} expenses.")