# Risk Management – VaR and Expected Shortfall Analysis

This repository contains the solution for the course project on market risk measurement using Value at Risk (VaR), Expected Shortfall (ES), option risk, and full repricing methods.

The main deliverable is a Jupyter notebook that answers all project questions with step-by-step calculations, written explanations, formulas, and supporting plots.

## Repository structure

### data/

#### xle_xlk_portfolio_dataset.csv
Cleaned historical dataset for the selected two-asset portfolio.  
It contains daily prices, individual asset returns, and portfolio returns for XLE and XLK.

### src/

#### VAR.ipynb
Main notebook containing the full project response, including markdown explanations, formulas, calculations, tables, VaR/ES estimations, option pricing, and plots.

### Root files

#### README.md
Project description and usage notes.

## Project content

The notebook covers the following topics:

- construction of a two-asset portfolio using XLE and XLK
- calculation of daily asset returns and portfolio returns
- estimation of portfolio expected return and volatility
- calculation of parametric VaR using SMA
- calculation of parametric VaR using EWMA
- selection and explanation of the EWMA decay factor λ
- calculation of non-parametric historical VaR
- calculation of hybrid VaR using exponentially weighted historical observations
- Monte Carlo simulation for VaR estimation
- comparison of VaR results across different methodologies
- conversion of daily VaR into weekly, monthly, and annual VaR
- calculation of VaR at the 10% confidence level
- stressed historical VaR using a crisis period
- calculation of Expected Shortfall using parametric and historical approaches
- comparison between VaR and Expected Shortfall
- simulation of GBM stock prices for option risk analysis
- estimation of option Greeks using Black-Scholes formulas
- Taylor delta-gamma approximation for option VaR
- Full Repricing VaR using historical shocks and Black-Scholes repricing
- comparison of Full Repricing VaR with Taylor VaR and parametric VaR
- interpretation of non-linear option risk

## Environment and requirements

Required packages:

- math
- random
- yfinance
- matplotlib
- Jupyter Notebook

Install the external packages with:

```bash
pip install yfinance matplotlib notebook
