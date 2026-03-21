# Risk Management – Bond Pricing and Yield Curve Analysis

This repository contains the solution for the course project focused on bond pricing and interest rate term structure using ECB data.

The main deliverable is a Jupyter notebook that answers the project questions with code and written explanations.

## Repository structure

data/
- ecb_spot_rates.csv  
  ECB spot rates extracted for a given date (semi-annual maturities up to 5 years).
- strip_prices.csv  
  Prices of STRIPS computed from spot rates.
- forward_rates.csv  
  Forward rates derived from the spot yield curve.

src/
- RM_responses.ipynb  
  Main notebook with markdown explanations and Python calculations.
  
README.md  
- This file.

## Methodology

The project includes:
- Extraction of ECB yield curve data
- Interpolation of spot rates
- Pricing of zero-coupon bonds (STRIPS)
- Computation of forward rates
- Pricing of a coupon bond using spot rates
- Clean and dirty price calculation

## Environment / requirements

Required packages:
- numpy
- pandas
- matplotlib