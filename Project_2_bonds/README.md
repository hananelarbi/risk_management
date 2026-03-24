# Risk Management – Bond Pricing and Yield Curve Analysis

This repository contains the solution for the course project on bond valuation, yield curve analysis, and hedging using ECB yield curve data.

The main deliverable is a Jupyter notebook that answers all project questions with step-by-step calculations, written explanations, and supporting plots.

## Repository structure

### `data/`

- `ecb_spot_rates.csv`  
  ECB AAA spot rates extracted for the selected date, using 10 consecutive semi-annual maturities from 0.5 to 5 years.

- `strip_prices.csv`  
  Prices of STRIPS computed from the selected spot rates.

- `forward_rates.csv`  
  Forward rates derived from the spot yield curve.

### `src/`

- `RM_responses.ipynb`  
  Main notebook containing the full project response, including markdown explanations, formulas, calculations, tables, and plots.

### Root files

- `README.md`  
  Project description and usage notes.

## Project content

The notebook covers the following topics:

- definition of a bond and its issuance process
- relationship between bond prices and interest rates
- extraction of ECB AAA spot yield curve data
- definition and interpretation of spot rates
- linear interpolation of spot yields
- pricing of STRIPS from spot rates
- derivation and interpretation of forward rates
- pricing of a coupon bond using spot rates
- pricing of the same bond using forward rates
- clean price and dirty price calculation
- estimation of yield to maturity
- calculation of DV01, duration, and convexity
- bond price sensitivity analysis under yield shocks
- construction of hedging strategies using DV01, duration, and convexity

## Environment and requirements

Required packages:

- `numpy`
- `pandas`
- `matplotlib`
