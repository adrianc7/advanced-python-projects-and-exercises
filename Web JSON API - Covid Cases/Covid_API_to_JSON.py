"""
Project Title: COVID-19 Data Analysis for US States
Date: September, 2024
Author: Adrian Chavez-Loya

Description:

This project involves the development of a Python application that leverages the COVID Tracking Project API to analyze daily COVID-19 statistics across various US states. The application retrieves JSON data from the API, processes it into a Python dictionary, and aggregates the information to calculate key statistics, including the average number of daily confirmed cases, dates with the highest new cases, and monthly trends.

The main features of the application include:

Dynamic State Retrieval: 
The program can handle multiple states by loading state codes from a text file, allowing for scalable data analysis.

Data Aggregation: 
It computes essential statistics such as average daily new cases, the date with the highest increase, the most recent date with zero new cases, and identifies the months with the highest and lowest new case counts.

JSON Output: 
The analyzed data for each state is saved to a JSON file in a designated directory, ensuring organized data management.

Error Handling: 
The application includes robust error handling to manage potential API request issues gracefully.

This project aims to provide insights into COVID-19 trends across the US and facilitates data-driven decision-making for public health. 
"""

import requests
import json
from datetime import datetime
from collections import defaultdict
import os

# Function to retrieve state/territory names from a text file
def load_state_codes(filename):
    """Loads state/territory codes from a text file and returns them as a list."""
    with open(filename, 'r') as file:
        states = [line.strip().lower() for line in file.readlines()]
    return states

# Function to save the retrieved data to a JSON file
def save_to_json(state, data):
    """Saves JSON data to a file named after the state in the specified directory."""
    directory = "HW5 Web JSON API - Covid cases/StateJSONFiles"
    os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist
    filename = os.path.join(directory, f'{state}.json')
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Saved statistics for {state} as: {filename}")

# Function to retrieve daily COVID information for the specified state
def retrieve_state_info(state):
    """Retrieves daily COVID information for the specified state."""
    state_daily_url = f'https://api.covidtracking.com/v1/states/{state}/daily.json'
    try:
        response = requests.get(state_daily_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data for state {state}: {e}")
        return None

# Function to analyze the COVID data and calculate statistics
def analyze_state_data(state_data):
    """Analyzes the COVID data and calculates statistics."""
    new_cases = []
    monthly_cases = defaultdict(int)
    highest_new_cases = 0
    highest_date = None
    recent_no_new_cases = None

    # Sort data by date in descending order to find the most recent date
    sorted_data = sorted(state_data, key=lambda d: d["date"], reverse=True)

    for entry in sorted_data:
        date = entry["date"]
        positive_increase = entry.get("positiveIncrease", 0)
        date_str = str(date)
        year_month = date_str[:6]  # Extract YYYYMM for monthly aggregation

        # Record the positive increase for average calculation
        new_cases.append(positive_increase)

        # Calculate monthly cases
        monthly_cases[year_month] += positive_increase

        # Check for highest new cases
        if positive_increase > highest_new_cases:
            highest_new_cases = positive_increase
            highest_date = date_str

        # Check for the most recent date with no new cases
        if positive_increase == 0 and not recent_no_new_cases:
            recent_no_new_cases = date_str

    # Calculate average new daily cases
    average_new_cases = sum(new_cases) / len(new_cases) if new_cases else 0

    # Find the month with the highest and lowest cases
    month_highest = max(monthly_cases, key=monthly_cases.get, default=None)

    # Filter out months with zero cases for lowest month calculation
    non_zero_months = {month: cases for month, cases in monthly_cases.items() if cases > 0}
    month_lowest = min(non_zero_months, key=non_zero_months.get) if non_zero_months else None

    # Format the results for printing
    highest_date_formatted = datetime.strptime(highest_date, "%Y%m%d").strftime("%Y/%m/%d") if highest_date else "N/A"
    recent_no_new_cases_formatted = datetime.strptime(recent_no_new_cases, "%Y%m%d").strftime("%Y/%m/%d") if recent_no_new_cases else "N/A"

    month_highest_formatted = f"{month_highest[:4]}/{month_highest[4:]}" if month_highest else "N/A"
    month_lowest_formatted = f"{month_lowest[:4]}/{month_lowest[4:]}" if month_lowest else "N/A"

    # Print the results in the required format
    print(f"State: {state_data[0]['state'].upper()}")
    print(f"Average Daily Cases: {average_new_cases:.2f}")
    print(f"Date With Highest Number of Cases: {highest_date_formatted} with {highest_new_cases} cases")
    print(f"Most Recent Date With No New Cases: {recent_no_new_cases_formatted}")
    print(f"Month With Highest Cases: {month_highest_formatted} with {monthly_cases.get(month_highest, 0)} cases")
    if month_lowest:
        print(f"Month With Lowest Cases: {month_lowest_formatted} with {monthly_cases[month_lowest]} cases")
    else:
        print("Month With Lowest Cases: N/A")
    print("-" * 40)

def main():
    """Main function that retrieves, analyzes, and saves COVID data for all states."""
    file_path = os.path.join('HW5 Web JSON API - Covid cases', 'states_territories.txt')
    state_codes = load_state_codes(file_path)

    for state in state_codes:
        print(f"\nProcessing data for state: {state.upper()}")
        state_data = retrieve_state_info(state)
        if state_data:
            analyze_state_data(state_data)
            save_to_json(state, state_data)


if __name__ == '__main__':
    main()
