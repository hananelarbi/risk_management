# Risk Management – Valuation and Hedging (Options)

This repository contains the solution for the course project “Valuation and Hedging – Options” using ASML as the underlying asset.  
The main deliverable is a Jupyter notebook that answers Questions 1–12 with code and written explanations.

## Repository structure

data/
- ASML_data.csv  
  Daily ASML market data (Date, OHLC, Close, Volume).
- ECB Data Portal_*.csv  
  ECB yield curve dataset used to extract the 1-year EUR spot rate (risk-free rate).

src/
- RM_responses.ipynb  
  Main notebook with markdown answers + Python calculations for Q1–Q12.
- download_data.py  
  Optional helper to download ASML data (not required to run the notebook if CSV is present).
- check_data.py  
  Optional helper to validate the dataset (shape, missing values, sorting).

README.md  
- This file.

## Data sources

Risk-free benchmark context:
- ECB Working Group on euro risk-free rates (€STR):  
  https://www.ecb.europa.eu/stats/euro-short-term-rates/interest_rate_benchmarks/WG_euro_risk-free_rates/html/index.en.html

Risk-free rate dataset used in the project:
- ECB yield curve 1-year spot rate series (continuous compounding), series key:  
  YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y  
  Dataset page:  
  https://data.ecb.europa.eu/data/datasets/YC/YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y

Random market option used for Q9 (gamma hedging):
- Euronext ASML stock options (AS9) contract specification (European style, 100 shares/contract, third-Friday expiry rule):  
  https://live.euronext.com/en/product/stock-options/AS9-DAMS/contract-specification  
- Option selected from the Mar 2026 option chain: call, strike 1200 EUR (as shown in the Euronext table view).

## Environment / requirements

Required packages:
- numpy
- pandas
