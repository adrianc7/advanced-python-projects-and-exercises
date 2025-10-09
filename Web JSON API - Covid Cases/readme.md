# Web JSON API – COVID Cases

## Overview
This project retrieves and saves COVID-19 data for all U.S. states and territories using the COVID Tracking Project API.  
The script reads each state code from a text file, requests daily COVID-19 data, processes it, prints statistics, and stores each state's full JSON response in `/StateJSONFiles`.  
If a state returns no data, the script notes this but continues with the rest.

---

## Tech Stack

| Category | Tools / Technologies |
|:--|:--|
| Language | Python |
| Libraries | requests · json · os · datetime · collections |
| Data Source | COVID Tracking Project API |
| Output Format | JSON |
| Concepts | REST API integration · Data ingestion · File automation · Error handling |

---

## Architecture

COVID Tracking Project API (per-state data)  
↓  
API Request for Each State  
↓  
Convert API Response → JSON  
↓  
Save to `/StateJSONFiles/<state>.json`  
↓  
Print Summary Statistics

---

## Repository Contents

| File / Folder | Description |
|:--|:--|
| `Covid_API_to_JSON.py` | Main script that retrieves COVID-19 data from the API, analyzes it, and writes JSON files per state. |
| `states_territories.txt` | List of state and territory codes for API requests. |
| `schema` | Description of expected JSON fields. |
| `/StateJSONFiles/` | Folder with one `.json` file for each U.S. state and territory (examples: `al.json`, `ar.json`, `as.json`). |

---

## Example Output (from `StateJSONFiles/ar.json`)

```json
{
  "date": 20210307,
  "state": "AR",
  "positive": 324818,
  "negative": 2480716,
  "hospitalizedCurrently": 335,
  "death": 5319,
  "recovered": 315517,
  "totalTestResults": 2736442
}
```
---

## How to Run

1. Ensure Python 3.x is installed.
2. Install dependencies:
   pip install requests
3. Verify that Covid_API_to_JSON.py and states_territories.txt are in the same directory.
4. Run the program:
   python Covid_API_to_JSON.py

---

## After Execution

- The console prints summary statistics for each state.
- Each state's full JSON data is saved in `/StateJSONFiles`.
- States returning no data still produce an empty JSON file for consistency.

---

## Workflow Summary

1. Load all state codes from `states_territories.txt`.
2. Request COVID-19 data from the API for each state.
3. Analyze results (average daily cases, peak date, zero-case dates, monthly totals).
4. Save each response as a JSON file and print statistics.
5. Handle errors and missing data without interrupting the script.

---

## Missing or Empty Results

Some territories (like American Samoa) return an empty object `{}` because no data was available.
The program still creates files to represent all states uniformly.

---

## Learning Outcomes

- Integrated a public API into a Python workflow.
- Learned to process and store structured JSON data programmatically.
- Applied basic error handling and data validation.

---
