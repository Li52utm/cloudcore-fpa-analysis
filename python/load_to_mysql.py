import pandas as pd
from sqlalchemy import create_engine

# --------------------------
# MySQL Connection
# --------------------------
USERNAME = "root"
PASSWORD = "612800"
HOST = "localhost"
DATABASE = "cloudcore_fpa"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
)

# --------------------------
# Load Customers
# --------------------------
customers = pd.read_csv("data/raw/customers.csv")

customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

print("✅ Customers loaded")

# --------------------------
# Load Employees
# --------------------------
employees = pd.read_csv("data/raw/employees.csv")

employees.to_sql(
    "employees",
    engine,
    if_exists="append",
    index=False
)

print("✅ Employees loaded")