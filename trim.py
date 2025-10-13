import pandas as pd

# Load the CSV
df = pd.read_csv("data/monthly_average_patronage_by_day_type_and_by_mode.csv")

# Filter for financial year 2024–25
filtered_df = df[
    ((df["Year"] == 2024) & (df["Month"] >= 7)) |  # July–Dec 2024
    ((df["Year"] == 2025) & (df["Month"] <= 6))    # Jan–June 2025
]

# Save the trimmed dataset
filtered_df.to_csv("patronage_2024_25.csv", index=False)
