# RWE Sustainability KPI Dashboard

## Project Overview

This project analyses publicly available RWE sustainability data from 2025 and converts it into a dashboard-ready KPI dataset.

The aim is to demonstrate sustainability data analysis, ESG-style KPI tracking, Python-supported data validation, Excel dashboarding, and structured project documentation using real public corporate sustainability reporting.

This project is designed as a portfolio project for sustainability, renewable energy, ESG reporting, project management, and data analysis roles.

## Project Outputs

This project includes:

- A cleaned RWE 2025 sustainability KPI dataset
- Python scripts for dataset validation, summary analysis, and chart generation
- An Excel dashboard for carbon, waste, materials, and circularity KPIs
- Dashboard screenshots for quick portfolio review
- Methodology and source documentation

## Dashboard Preview

The Excel dashboard summarises key RWE 2025 sustainability indicators, including:

- Total GHG emissions
- Scope 1, Scope 2, and Scope 3 emissions
- Total waste generated
- Hazardous and non-recycled waste
- Material use and secondary materials
- Circularity indicators
- Biodiversity target notes

## Screenshots

![Excel Dashboard Overview](powerbi/dashboard_screenshots/excel_dashboard_overview.png)

![Carbon Emissions Chart](powerbi/dashboard_screenshots/carbon_emissions_chart.png)

![Waste Indicators Chart](powerbi/dashboard_screenshots/waste_indicators_chart.png)

![Materials Breakdown Chart](powerbi/dashboard_screenshots/materials_breakdown_chart.png)

## Data Source

The dataset is based on public RWE Group sustainability reporting for 2025.

Main sources:

- RWE Annual Report 2025
- RWE Sustainability Key Figures Report 2025
- RWE Group Sustainability Reporting – Data 2025

## Data Scope

The dataset uses RWE Group-level sustainability indicators. It does not represent confidential company data or internal project-level offshore wind farm data.

The project focuses on:

- Carbon emissions
- Waste indicators
- Materials and circularity
- Biodiversity targets

## Tools Used

- Python
- pandas
- matplotlib
- Microsoft Excel
- Power BI-ready dataset structure
- GitHub

## Repository Structure

```text
data/
  rwe_sustainability_kpi_2025.csv

docs/
  methodology.md
  sources.md

excel/
  rwe_sustainability_kpi_dashboard.xlsx

src/
  check_dataset.py
  summary_analysis.py
  create_charts.py

powerbi/
  dashboard_screenshots/

requirements.txt
README.md
