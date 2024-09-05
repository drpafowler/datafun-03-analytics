'''
This  script is all about fetching data from different places on the interweb

The four types of data sources are: CSV, Excel, JSON, and Text.

'''

######################
# Import Libraries
######################

import csv
import json
import pathlib
import requests


######################
# Declare Global Variables
######################


######################
# Function Definitions CSV
######################

def fetch_csv_file(folder_name:str, filename:str, url:str) -> None:
    '''
    This function fetches a CSV file from the internet and saves it to a local folder.
    '''
    # Fetch the CSV file from the internet
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Save the CSV file to the local folder
        with open(f'{folder_name}/{filename}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to fetch the CSV file from {url}')

def write_csv_file(folder_name:str, filename:str, string_data:str) -> None:
    '''
    This function writes a CSV file to a local folder.
    '''
    # Save the CSV file to the local folder
    with open(f'{folder_name}/{filename}', 'w') as file:
        file.write(string_data)

######################
# Function Definitions Excel
######################

def fetch_excel_file(folder_name:str, filename:str, url:str) -> None:
    '''
    This function fetches an Excel file from the internet and saves it to a local folder.
    '''
    # Fetch the Excel file from the internet
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Save the Excel file to the local folder
        with open(f'{folder_name}/{filename}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to fetch the Excel file from {url}')

######################
# Function Definitions JSON
######################

def fetch_json_file(folder_name:str, filename:str, url:str) -> None:
    '''
    This function fetches a JSON file from the internet and saves it to a local folder.
    '''
    # Fetch the JSON file from the internet
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Save the JSON file to the local folder
        with open(f'{folder_name}/{filename}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to fetch the JSON file from {url}')

######################
# Function Definitions Text
######################

def fetch_text_file(folder_name:str, filename:str, url:str) -> None:
    '''
    This function fetches a text file from the internet and saves it to a local folder.
    '''
    # Fetch the text file from the internet
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Save the text file to the local folder
        with open(f'{folder_name}/{filename}', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to fetch the text file from {url}')

######################
# Main Function
######################

def main():