import pandas as pd
from pathlib import Path

DATA_PATH = Path("../data/rwe_sustainability_kpi_2025.csv")

def check_dataset():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values by column:")
    print(df.isnull().sum())

    print("\nKPI categories:")
    print(df["kpi_category"].value_counts())

    print("\nYear values:")
    print(df["year"].value_counts().sort_index())

    print("\nPreview:")
    print(df.head())

if __name__ == "__main__":
    check_dataset()
