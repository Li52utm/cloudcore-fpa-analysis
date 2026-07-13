import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker()
random.seed(42)
Faker.seed(42)

# -----------------------------
# Create output folder
# -----------------------------

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)
# -----------------------------
# Customers
# -----------------------------

industries = [
    "Healthcare",
    "Finance",
    "Retail",
    "Technology",
    "Manufacturing",
    "Education"
]

company_sizes = [
    "Small",
    "Medium",
    "Large",
    "Enterprise"
]

customers = []

for customer_id in range(1, 501):

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.company(),
        "industry": random.choice(industries),
        "region_id": random.randint(1,4),
        "company_size": random.choice(company_sizes)
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    output_folder / "customers.csv",
    index=False
)

print("✅ customers.csv created")

# -----------------------------
# Employees
# -----------------------------

first_names = [
    "James","John","Robert","Michael","David",
    "Sarah","Emily","Jessica","Ashley","Olivia",
    "Daniel","Matthew","Andrew","Sophia","Emma"
]

last_names = [
    "Smith","Johnson","Williams","Brown",
    "Jones","Garcia","Miller","Davis",
    "Wilson","Taylor","Anderson"
]

employees = []

for employee_id in range(1,151):

    employees.append({
        "employee_id": employee_id,
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "department_id": random.randint(1,8),
        "hire_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        "salary": random.randint(55000,180000)
    })

employees_df = pd.DataFrame(employees)

employees_df.to_csv(
    output_folder / "employees.csv",
    index=False
)

print("✅ employees.csv created")
# -----------------------------
# Revenue
# -----------------------------

from datetime import datetime

subscription_prices = {
    "Basic": 150,
    "Pro": 500,
    "Enterprise": 2500
}

months = pd.date_range(
    "2024-01-01",
    "2026-04-01",
    freq="MS"
)

revenue = []

revenue_id = 1

for month in months:

    growth = 1 + ((month.year - 2024) * 0.18)

    if month.month in [10,11,12]:
        seasonality = 1.20
    elif month.month in [1,2]:
        seasonality = 0.90
    else:
        seasonality = 1.00

    for customer in customers:

        tier = random.choices(
            ["Basic","Pro","Enterprise"],
            weights=[65,25,10]
        )[0]

        amount = subscription_prices[tier]

        amount *= growth
        amount *= seasonality
        amount *= random.uniform(0.95,1.05)

        revenue.append({

            "revenue_id": revenue_id,

            "customer_id": customer["customer_id"],

            "product_id":
                {"Basic":1,"Pro":2,"Enterprise":3}[tier],

            "revenue_date": month,

            "amount": round(amount,2)

        })

        revenue_id += 1

revenue_df = pd.DataFrame(revenue)

revenue_df.to_csv(
    output_folder / "revenue.csv",
    index=False
)

print("✅ revenue.csv created")