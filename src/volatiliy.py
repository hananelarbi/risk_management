from pathlib import Path
import pandas as pd
import numpy as np

# Load data
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR.parent / "data" / "ASML_data.csv"
df = pd.read_csv(csv_path)
df["Date"] = pd.to_datetime(df["Date"])

# Risk-free rate (annual, euro proxy)
r = 0.02

# Maturity in years
T = 1.0

# Compute log-returns
df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
df = df.dropna()

# Volatility over a window consistent with T
window_days = int(252 * T)
returns_window = df["log_return"].tail(window_days)

sigma_daily = returns_window.std()
sigma_annual = sigma_daily * np.sqrt(252)

print(f"Risk-free rate (r): {r}")
print(f"Maturity (T): {T}")
print(f"Daily volatility: {sigma_daily}")
print(f"Annualized volatility: {sigma_annual}")


#