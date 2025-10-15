# Cryptocurrency Arbitrage Detection Program

## Overview
This Cryptocurrency Arbitrage Detection Program analyzes exchange rate relationships between major cryptocurrencies to identify potential arbitrage opportunities.  
By fetching real-time pricing data from the *CoinGecko API* and representing currencies as nodes in a directed graph, the program detects pricing inconsistencies that could theoretically yield profit through circular trading paths.

This project demonstrates skills in data ingestion, graph theory, and financial analytics using Python, focusing on data-driven detection of arbitrage patterns.

---

## Tech Stack

| Category | Tools / Libraries |
|:--|:--|
| API Source | CoinGecko REST API |
| Language | Python |
| Libraries | requests · networkx · matplotlib · pandas |
| Concepts | Graph algorithms · Real-time data ingestion · Arbitrage analysis |

---

## Architecture

Real-Time Exchange Data (CoinGecko API)  
↓  
Data Ingestion (Python requests)  
↓  
Graph Construction (NetworkX Directed Graph)  
↓  
Path and Weight Analysis (Forward & Reverse Exchange Rates)  
↓  
Arbitrage Detection & Visualization (Matplotlib)

---

## Repository Contents

| File | Description |
|:--|:--|
| [cryptotrade.ipynb](cryptotrade.ipynb) | Jupyter Notebook implementing the full pipeline: data fetching, graph construction, path analysis, and arbitrage detection. |
| [cryptocurrency-arbitrage-detection-program.pdf](cryptocurrency-arbitrage-detection-program.pdf) | PDF version of Notebook |

---

## Key Features

- **Live Data Ingestion:** Retrieves current cryptocurrency prices (USD pairs) from CoinGecko.  
- **Graph-Based Modeling:** Builds a directed graph where edges represent exchange rates.  
- **Arbitrage Detection:** Compares forward and reverse exchange paths to find pricing imbalances.  
- **Visualization:** Generates a network graph showing relationships between currencies.  
- **Insights Summary:** Reports smallest and largest price ratio deviations, signaling potential arbitrage opportunities.

---

## Results Summary

- Constructed a currency exchange graph with USD as the central node.  
- All analyzed paths showed **equilibrium (factor ≈ 1.0)**, **indicating **no real-time arbitrage opportunities under current market conditions**.  
- The system structure supports future extensions for continuous monitoring or multi-market analysis.

---

## Learning Outcomes

- Applied graph algorithms to real-world financial data.  
- Integrated REST APIs for live data analysis.  
- Explored graph-based reasoning for currency exchange and arbitrage.  
- Practiced transforming notebook analytics into an interpretable financial insights report.

---

## Future Improvements

- Expand to include crypto-to-crypto exchange rates, not just USD pairs.  
- Implement asynchronous API requests for faster data refresh.  
- Develop real-time alerting for arbitrage threshold triggers.

