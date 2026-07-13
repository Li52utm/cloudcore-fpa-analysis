import pandas as pd
import random
from pathlib import Path

random.seed(42)

# -----------------------------
# Load Customers
# -----------------------------

customers = pd.read_csv("data/raw/customers.csv")

# -----------------------------
# Products
# -----------------------------

products = {
    1: 49.00,     # Starter
    2: 149.00,    # Professional
    3: 399.00,    # Business
    4: 2999.00    # Enterprise
}

# -----------------------------
# Date Range
# -----------------------------

months = pd.date_range(
    start="2024-01-01",
    end="2026-04-01",
    freq="MS"
)

revenue = []

revenue_id = 1
for month in months:

    for _, customer in customers.iterrows():

        # Most customers stay on one product
        product_id = random.choices(
            [1,2,3,4],
            weights=[45,30,20,5]
        )[0]

        amount = products[product_id]

        # Small monthly variation
        amount *= random.uniform(0.95,1.05)

        # Company growth
        months_since_start = (
            (month.year-2024)*12
            + month.month
        )

        growth = 1 + (months_since_start * 0.01)

        amount *= growth

        revenue.append({

            "revenue_id": revenue_id,

            "customer_id": customer["customer_id"],

            "product_id": product_id,

            "revenue_date": month.date(),

            "amount": round(amount,2)

        })

        revenue_id += 1
        revenue_df = pd.DataFrame(revenue)

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

revenue_df.to_csv(
    output_folder / "revenue.csv",
    index=False
)

print(f"Generated {len(revenue_df)} revenue rows.")