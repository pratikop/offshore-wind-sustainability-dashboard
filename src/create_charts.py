import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("../data/rwe_sustainability_kpi_2025.csv")
OUTPUT_DIR = Path("../powerbi/dashboard_screenshots")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    return pd.read_csv(DATA_PATH)

def create_carbon_chart(df):
    carbon_items = [
        "Gross Scope 1 GHG emissions",
        "Gross location-based Scope 2 GHG emissions",
        "Total gross indirect Scope 3 GHG emissions"
    ]

    carbon = df[df["kpi_name"].isin(carbon_items)]

    plt.figure(figsize=(8, 5))
    plt.bar(carbon["kpi_name"], carbon["value"])
    plt.title("RWE 2025 GHG Emissions by Scope")
    plt.ylabel("Million metric tons CO2e")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "carbon_emissions_by_scope.png")
    plt.close()

def create_waste_chart(df):
    waste_items = [
        "Non-recycled waste non-hazardous",
        "Non-recycled waste hazardous",
        "Hazardous waste total"
    ]

    waste = df[df["kpi_name"].isin(waste_items)]

    plt.figure(figsize=(8, 5))
    plt.bar(waste["kpi_name"], waste["value"])
    plt.title("RWE 2025 Waste Indicators")
    plt.ylabel("Thousand metric tons")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "waste_indicators.png")
    plt.close()

def create_material_chart(df):
    material_items = [
        "Ferrous metal mainly steel",
        "Concrete",
        "Non-ferrous metal mainly aluminium and copper",
        "Polymers",
        "Glass",
        "Other materials"
    ]

    materials = df[df["kpi_name"].isin(material_items)]

    plt.figure(figsize=(9, 5))
    plt.bar(materials["kpi_name"], materials["value"])
    plt.title("RWE 2025 Product Material Breakdown")
    plt.ylabel("Metric tons")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "material_breakdown.png")
    plt.close()

def main():
    df = load_data()

    create_carbon_chart(df)
    create_waste_chart(df)
    create_material_chart(df)

    print("Charts created successfully.")
    print(f"Saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
