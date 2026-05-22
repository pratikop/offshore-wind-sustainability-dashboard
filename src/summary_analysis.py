import pandas as pd
from pathlib import Path

DATA_PATH = Path("../data/rwe_sustainability_kpi_2025.csv")

def load_data():
    return pd.read_csv(DATA_PATH)

def print_carbon_summary(df):
    carbon = df[df["kpi_category"] == "Carbon"]

    print("\nCARBON SUMMARY")
    print("-" * 40)

    for _, row in carbon.iterrows():
        print(f"{row['kpi_name']}: {row['value']} {row['unit']}")

def print_waste_summary(df):
    waste = df[df["kpi_category"] == "Waste"]

    print("\nWASTE SUMMARY")
    print("-" * 40)

    total_waste = waste[waste["kpi_name"] == "Total waste generated"]["value"].sum()
    hazardous_waste = waste[waste["kpi_name"] == "Hazardous waste total"]["value"].sum()

    print(f"Total waste generated: {total_waste} thousand metric tons")
    print(f"Hazardous waste total: {hazardous_waste} thousand metric tons")

    if total_waste > 0:
        hazardous_share = (hazardous_waste / total_waste) * 100
        print(f"Hazardous waste share: {hazardous_share:.2f}%")

def print_circularity_summary(df):
    circularity = df[df["kpi_category"] == "Circularity"]

    print("\nCIRCULARITY SUMMARY")
    print("-" * 40)

    for _, row in circularity.iterrows():
        print(f"{row['kpi_name']}: {row['value']} {row['unit']}")

def main():
    df = load_data()

    print("RWE Sustainability KPI Analysis - 2025")
    print("=" * 40)

    print_carbon_summary(df)
    print_waste_summary(df)
    print_circularity_summary(df)

if __name__ == "__main__":
    main()
