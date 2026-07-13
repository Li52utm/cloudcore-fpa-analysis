import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# MySQL Connection
# -----------------------------
USERNAME = "root"
PASSWORD = "612800"
HOST = "localhost"
DATABASE = "cloudcore_fpa"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
)

files = [
    "customers",
    "employees",
    "revenue",
    "expenses",
    "budget",
    "forecast"
]

for table in files:

    print(f"Loading {table}...")

    df = pd.read_csv(f"data/raw/{table}.csv")

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

    print(f"✅ {table} loaded")

print("\nAll data imported successfully!")