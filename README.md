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

## Environment / requirements

Required packages:
- numpy
- pandas

