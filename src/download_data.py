import yfinance as yf
import pandas as pd

ticker = "ASML"

data = yf.download(ticker, start="2018-01-01", end="2025-01-01")

print(data.head())

data.to_csv("ASML_data.csv")

print("Téléchargement terminé !")
