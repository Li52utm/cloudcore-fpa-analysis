import pandas as pd
import random
from pathlib import Path

random.seed(42)

months = pd.date_range(
    start="2024-01-01",
    end="2026-04-01",
    freq="MS"
)

forecast = []

forecast_id = 1

base = 280000

for i, month in enumerate(months):

    revenue = base * (1 + i * 0.015)

    revenue *= random.uniform(0.98,1.02)

    forecast.append({
        "forecast_id": forecast_id,
        "forecast_month": month.date(),
        "expected_revenue": round(revenue,2)
    })

    forecast_id += 1

forecast_df = pd.DataFrame(forecast)

Path("data/raw").mkdir(parents=True, exist_ok=True)

forecast_df.to_csv(
    "data/raw/forecast.csv",
    index=False
)

print(f"Generated {len(forecast_df)} forecast rows.")