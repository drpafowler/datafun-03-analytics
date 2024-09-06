'''
This  script is all about fetching data from different places on the interweb

The four types of data sources are: CSV, Excel, JSON, and Text.

'''

######################
# Import Libraries
######################

import csv
import json     
import pathlib as pl
import requests 
import pandas as pd
import pathlib 
import utils_philip
import philip_project


######################
# Declare Global Variables
######################

fetched_folder_name = "fetched"

######################
# Function Definitions CSV
######################

def fetch_csv_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch csv data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_csv_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_csv_file(folder_name, filename, response.content)
        print(f"SUCCESS: Csv file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching csv data: {e}")

def write_csv_file(folder_name:str, filename:str, binary_data:bytes) -> None:
    """Write csv binary_data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_csv_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        print(f"SUCCESS: csv data saved to {file_path}")
    except IOError as e:
        print(f"Error writing csv data to {file_path}: {e}")  

######################
# Function Definitions Excel
######################

def fetch_excel_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch Excel data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_excel_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_excel_file(folder_name, filename, response.content)
        print(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Excel data: {e}")

def write_excel_file(folder_name:str, filename:str, binary_data:bytes) -> None:
    """Write Excel binary_data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_excel_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        print(f"SUCCESS: Excel data saved to {file_path}")
    except IOError as e:
        print(f"Error writing Excel data to {file_path}: {e}")    

######################
# Function Definitions JSON
######################

def fetch_json_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch JSON data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_json_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_json_file(folder_name, filename, response.json())
        print(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON data: {e}")

def write_json_file(folder_name:str, filename:str, json_data) -> None:
    """Write JSON data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_json_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        print(f"SUCCESS: JSON data saved to {file_path}")
    except IOError as e:
        print(f"Error writing JSON data to {file_path}: {e}")

######################
# Function Definitions Text
######################

def fetch_txt_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch text data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_csv_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_txt_file(folder_name, filename, response.content)
        print(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching txt data: {e}")

def write_txt_file(folder_name:str, filename:str, binary_data:bytes) -> None:
    """Write txt binary_data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_txt_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        print(f"SUCCESS: txt data saved to {file_path}")
    except IOError as e:
        print(f"Error writing txt data to {file_path}: {e}")  


######################
# Main Function
######################

def main():
    
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Reuse get_byline() from imported module
    print(f"Byline: {utils_philip.get_byline()}")

    # Reuse  create_folders_from_list() from imported module to make a folder for fetched files
    # We set the name as a global variable so the whole module can use it. 
    # Make sure we provide a LIST when using our function
    philip_project.create_folders_from_list([fetched_folder_name])

    # Web locations of different types of data to fetch
    excel_url:str = 'https://github.com/prasertcbs/basic-dataset/raw/master/cars.xlsx' 
    json_url:str = 'https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/students.json'
    txt_url:str = 'https://raw.githubusercontent.com/mmcky/nyu-econ-370/master/notebooks/data/book-war-and-peace.txt'
    csv_url:str = 'https://raw.githubusercontent.com/jack-madison/Cycling-Data/main/losangeles_ca/bike_share/la_daily_bikeshare.csv' 

    # Fetch data files - provide the fetched file names
    fetch_excel_file(fetched_folder_name, "cars.xlsx", excel_url)
    fetch_json_file(fetched_folder_name, "students.json", json_url)
    fetch_txt_file(fetched_folder_name, "warpeace.txt", txt_url)
    fetch_csv_file(fetched_folder_name, "bikes.csv", csv_url)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


######################
# Conditional Execution
######################

if __name__ == '__main__':
    main()