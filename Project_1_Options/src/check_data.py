from pathlib import Path
import pandas as pd

# Get absolute path to this script's directory
BASE_DIR = Path(__file__).resolve().parent

# Build path to data file (go one level up, then into data folder)
csv_path = BASE_DIR.parent / "data" / "ASML_data.csv"

# Load dataset
df = pd.read_csv(csv_path)

print("Dimensions:", df.shape)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nColumn types:")
print(df.dtypes)

print("\nNumber of duplicate rows:", df.duplicated().sum())

# Check that dates are properly sorted
df["Date"] = pd.to_datetime(df["Date"])
is_sorted = df["Date"].is_monotonic_increasing
print("\nDates sorted correctly?", is_sorted)
