from pathlib import Path
import pandas as pd
import numpy as np

# Build a robust path to the CSV file (works no matter where the script is run from)
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR.parent / "data" / "ASML_data.csv"

# Load dataset
df = pd.read_csv(csv_path)
df["Date"] = pd.to_datetime(df["Date"])

# Compute daily log-returns
df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
df = df.dropna()

print("Price statistics:")
print(df["Close"].describe())

print("\nReturn statistics:")
print(df["log_return"].describe())

print("\nSkewness:", df["log_return"].skew())
print("Kurtosis:", df["log_return"].kurt())
