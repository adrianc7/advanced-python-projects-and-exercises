# Stock Market Trading Automation (Paper Trading)

## Overview
This Stock Market Trading Automation project simulates algorithmic trading strategies using historical and real-time data from the Alpaca API.  
It evaluates multiple strategies—SMA Crossover, Mean Reversion, and Volatility Breakout—across 10 major U.S. equities in a paper trading environment, identifying which combination of stock and strategy yields the best simulated profit.

This project highlights skills in data ingestion, technical indicator design, and Python automation, offering a framework for scalable algorithmic trading research.

---

## Tech Stack

| Category | Tools / Libraries |
|:--|:--|
| API Source | Alpaca Trade API |
| Language | Python |
| Libraries | pandas · json · alpaca-trade-api |
| Data | Historical daily stock data (CSV files in `/data/`) |
| Concepts | Technical Indicators · Automated Trading · Simulation · Scheduling |

---

## Architecture

Historical / Live Market Data (Alpaca API or `/data/*.csv`)  
↓  
Data Loading and Cleaning (pandas)  
↓  
Strategy Simulation (SMA · Mean Reversion · Volatility Breakout)  
↓  
Result Logging (`results.json`)  
↓  
Automation via Scheduled Execution (cron / task scheduler)

---

## Repository Contents

| File / Folder | Description |
|:--|:--|
| **final_project.py** | Core script that retrieves stock data, applies all trading strategies, calculates profit/loss, and logs the best result. |
| **results.json** | Automatically generated file storing the top-performing strategy, stock, and profit from the simulation. |
| **Project Title: Stock Market Trading Automation (Paper Trading).pdf** | Formal report summarizing objectives, methodology, strategy logic, results, and project insights. |
| **"data" folder** | Folder containing 10 historical stock CSV files used for backtesting and offline testing. Each file includes `Date`, `Open`, `High`, `Low`, `Close`, and `Volume` columns. |

---

## Trading Strategies Implemented

### **1. SMA (Simple Moving Average) Crossover**
- Buys when the short-term SMA rises above the long-term SMA.  
- Sells when the crossover reverses.  
- Captures momentum and short-term trend shifts.

### **2. Mean Reversion**
- Calculates rolling mean and standard deviation to identify overbought or oversold signals.  
- Buys when price dips below the lower band; sells when it exceeds the upper band.  
- Designed for range-bound price patterns.

### **3. Volatility Breakout**
- Detects strong directional moves by comparing price changes to a volatility multiplier.  
- Enters trades when daily price range exceeds a breakout threshold.  
- Targets high-volatility stocks.

---

## Example Output (`results.json`)
```json
{
  "Best Strategy": "Mean Reversion",
  "Stock": "NFLX",
  "Profit": 130.02
}
```

---

## Results Summary
- Simulated 3 strategies across 10 major U.S. equities using Alpaca and historical data.  
- Best-performing combination: *Mean Reversion on NFLX* (+$130 simulated profit).  
- Demonstrated the ability to backtest, rank, and compare quantitative trading methods.  
- Validated pipeline for transition to live algorithmic trading environments.

---

## Key Features
- **Offline Testing:** Use `/data/*.csv` for historical backtesting or live data from Alpaca.  
- **Multi-Strategy Evaluation:** Compare and log performance across multiple algorithmic models.  
- **Paper Trading Environment:** Safely simulate trades without risking capital.  
- **JSON Reporting:** Automatically records top results for tracking or dashboard display.  
- **Modular Design:** Easily extendable to include additional strategies or asset classes.

---

## Learning Outcomes
- Built an automated trading simulation framework in Python.  
- Applied technical indicators to assess strategy performance.  
- Practiced algorithmic thinking and data-driven decision evaluation.  
- Gained exposure to financial APIs, logging, and performance reporting.

---

## Potential Future Improvements
- Enable real-time trading mode with live Alpaca credentials.  
- Integrate additional indicators (RSI, MACD, Bollinger Bands).  
- Visualize cumulative returns and equity curves with matplotlib.  
- Store trade history in a SQL database for long-term performance tracking.  
- Deploy as a cloud-scheduled job (AWS Lambda or Azure Function) for daily execution.

