# WEEK 4 – CAPSTONE PROJECT (Option 2)
# COVID-19 Data Tracker
#
# Tasks:
# 1. Load the COVID-19 dataset using Pandas.
# 2. Display the top 5 countries by total confirmed cases.
# 3. Plot a bar chart using Matplotlib.
#
# Required libraries:
# pip install pandas matplotlib

import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "covid_data.csv"
DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"


def load_data():
    """Load the dataset from a local CSV file or download it from OWID."""
    if os.path.exists(DATA_FILE):
        print(f"Loading dataset from {DATA_FILE}...")
        return pd.read_csv(DATA_FILE)

    print("Local dataset not found. Downloading the OWID COVID-19 dataset...")
    try:
        data = pd.read_csv(DATA_URL)
        # Save a local copy so the dataset does not need to be downloaded again.
        data.to_csv(DATA_FILE, index=False)
        print(f"Dataset downloaded and saved as {DATA_FILE}.")
        return data
    except Exception as error:
        raise RuntimeError(
            "Could not download the dataset. Check your internet connection "
            f"or download the OWID CSV and save it as '{DATA_FILE}'."
        ) from error


def get_top_five_countries(data):
    """Get each country's latest available total case count and return top five."""
    required_columns = {"location", "date", "total_cases"}
    missing = required_columns - set(data.columns)

    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(sorted(missing))}")

    # Remove aggregate rows such as 'World' and regional groupings.
    if "iso_code" in data.columns:
        data = data[~data["iso_code"].astype(str).str.startswith("OWID_")]

    data = data.copy()
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data["total_cases"] = pd.to_numeric(data["total_cases"], errors="coerce")
    data = data.dropna(subset=["location", "date", "total_cases"])

    if data.empty:
        raise ValueError("No valid country case records were found in the dataset.")

    # Use the latest non-empty total_cases value recorded for each country.
    latest_records = (
        data.sort_values("date")
        .groupby("location", as_index=False)
        .tail(1)
    )

    top_five = latest_records.nlargest(5, "total_cases")
    return top_five[["location", "date", "total_cases"]].sort_values(
        "total_cases", ascending=False
    )


def display_results(top_five):
    """Print the top five countries in a readable table."""
    print("\n========== TOP 5 COUNTRIES BY TOTAL COVID-19 CASES ==========")
    print(f"{'Rank':<8}{'Country':<25}{'Total Cases':>20}")
    print("-" * 53)

    for rank, (_, row) in enumerate(top_five.iterrows(), start=1):
        cases = f"{row['total_cases']:,.0f}"
        print(f"{rank:<8}{row['location']:<25}{cases:>20}")

    print("\nLatest data dates used:")
    for _, row in top_five.iterrows():
        print(f"- {row['location']}: {row['date'].date()}")


def plot_chart(top_five):
    """Create and save a bar chart for the top five countries."""
    plt.figure(figsize=(10, 6))
    bars = plt.bar(top_five["location"], top_five["total_cases"])

    plt.title("Top 5 Countries by Total Confirmed COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Confirmed Cases")
    plt.xticks(rotation=25, ha="right")
    plt.ticklabel_format(style="plain", axis="y")

    # Display the case count above each bar.
    for bar, value in zip(bars, top_five["total_cases"]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.tight_layout()
    plt.savefig("covid_top_5_countries.png", dpi=300)
    print("\nBar chart saved as covid_top_5_countries.png")
    plt.show()


def main():
    try:
        covid_data = load_data()
        top_five = get_top_five_countries(covid_data)
        display_results(top_five)
        plot_chart(top_five)
    except (RuntimeError, ValueError, OSError) as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
