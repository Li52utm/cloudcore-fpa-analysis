import pandas as pd
import random
from pathlib import Path

random.seed(42)

departments = {
    1: "Sales",
    2: "Marketing",
    3: "Finance",
    4: "Engineering",
    5: "Operations"
}

months = pd.date_range(
    start="2024-01-01",
    end="2026-04-01",
    freq="MS"
)

budget = []

budget_id = 1

for month in months:

    for dept in departments:

        base_budget = {
            1: 120000,
            2: 80000,
            3: 60000,
            4: 150000,
            5: 90000
        }

        amount = base_budget[dept]

        # small variation
        amount *= random.uniform(0.97, 1.03)

        budget.append({
            "budget_id": budget_id,
            "budget_month": month.date(),
            "department_id": dept,
            "budget_amount": round(amount,2)
        })

        budget_id += 1

budget_df = pd.DataFrame(budget)

Path("data/raw").mkdir(parents=True, exist_ok=True)

budget_df.to_csv(
    "data/raw/budget.csv",
    index=False
)

print(f"Generated {len(budget_df)} budget rows.")