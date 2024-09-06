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
import re
from collections import Counter
import requests 
import pandas as pd
import pathlib 
import utils_philip
import philip_project
import matplotlib.pyplot as plt
import openpyxl

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

def display_first_five_lines_csv(folder_name: str, filename: str) -> None:
    """Open a CSV file and display the first five lines using pandas."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: display_first_five_lines with file_path={file_path}")
    try:
        df = pd.read_csv(file_path)
        print(df.head(5))
    except IOError as e:
        print(f"Error reading csv file {file_path}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: No data in csv file {file_path}: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing csv file {file_path}: {e}")

def create_histogram_for_bikes(folder_name: str, filename: str) -> None:
    """Create a histogram for date and ride_count using the bikes.csv file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: create_histogram_for_bikes with file_path={file_path}")
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Convert the 'date' column to datetime format if necessary
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        
        # Create a histogram for the 'ride_count' column
        plt.figure(figsize=(10, 6))
        plt.hist(df['ride_count'], bins=30, edgecolor='black')
        plt.title('Histogram of Ride Count')
        plt.xlabel('Ride Count')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
        
    except IOError as e:
        print(f"Error reading csv file {file_path}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: No data in csv file {file_path}: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing csv file {file_path}: {e}")

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

def display_first_five_lines_xlsx(folder_name: str, filename: str) -> None:
    """Open an XLSX file and display the first five lines using pandas."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: display_first_five_lines_xlsx with file_path={file_path}")
    try:
        df = pd.read_excel(file_path)
        print(df.head(5))
    except IOError as e:
        print(f"Error reading xlsx file {file_path}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: No data in xlsx file {file_path}: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing xlsx file {file_path}: {e}")

def convert_xlsx_to_csv(folder_name: str, xlsx_filename: str, csv_filename: str) -> None:
    """Convert an XLSX file to a CSV file."""
    xlsx_file_path = pathlib.Path(folder_name).joinpath(xlsx_filename)
    csv_file_path = pathlib.Path(folder_name).joinpath(csv_filename)
    print(f"FUNCTION CALLED: convert_xlsx_to_csv with xlsx_file_path={xlsx_file_path} and csv_file_path={csv_file_path}")
    try:
        # Read the XLSX file
        df = pd.read_excel(xlsx_file_path)
        
        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        print(f"Successfully converted {xlsx_filename} to {csv_filename}")
    except IOError as e:
        print(f"Error reading or writing file: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: No data in xlsx file {xlsx_file_path}: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing xlsx file {xlsx_file_path}: {e}")

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

def display_json_data(folder_name: str, filename: str) -> None:
    """Read and display JSON data from a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: display_json_data with file_path={file_path}")
    try:
        with file_path.open('r', encoding='utf-8') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4, sort_keys=True))
    except IOError as e:
        print(f"Error reading json file {file_path}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding json file {file_path}: {e}")

def display_json_data_sorted_by_craft(folder_name: str, filename: str) -> None:
    """Read, sort by craft, and display JSON data from a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: display_json_data_sorted_by_craft with file_path={file_path}")
    try:
        with file_path.open('r', encoding='utf-8') as file:
            data = json.load(file)
            # Sort the people by craft
            if "people" in data:
                data["people"] = sorted(data["people"], key=lambda x: x["craft"])
            # Pretty-print the sorted JSON data
            sorted_data = json.dumps(data, indent=4, sort_keys=True)
            print(sorted_data)
    except IOError as e:
        print(f"Error reading json file {file_path}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding json file {file_path}: {e}")

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

def find_top_10_common_words(folder_name: str, filename: str) -> None:
    """Find the top 10 most common words in a TXT file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: find_top_10_common_words with file_path={file_path}")
    try:
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
            # Use regex to find words and convert to lowercase
            words = re.findall(r'\b\w+\b', text.lower())
            # Count the frequency of each word
            word_counts = Counter(words)
            # Get the 10 most common words
            common_words = word_counts.most_common(10)
            print("Top 10 most common words:")
            for word, count in common_words:
                print(f"{word}: {count}")
    except IOError as e:
        print(f"Error reading txt file {file_path}: {e}")

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
    json_url:str = 'http://api.open-notify.org/astros.json'
    txt_url:str = 'https://raw.githubusercontent.com/mmcky/nyu-econ-370/master/notebooks/data/book-war-and-peace.txt'
    csv_url:str = 'https://raw.githubusercontent.com/jack-madison/Cycling-Data/main/losangeles_ca/bike_share/la_daily_bikeshare.csv' 

    # Fetch data files - provide the fetched file names
    fetch_excel_file(fetched_folder_name, "cars.xlsx", excel_url)
    fetch_json_file(fetched_folder_name, "astros.json", json_url)
    fetch_txt_file(fetched_folder_name, "warpeace.txt", txt_url)
    fetch_csv_file(fetched_folder_name, "bikes.csv", csv_url)

    # Display the first five lines of the fetched CSV file
    display_first_five_lines_csv(fetched_folder_name, "bikes.csv")
    
    #display_first_five_lines_xlsx(fetched_folder_name, "cars.xlsx") - I can't seem to make this work see the following
    #Convert the XLSX to CSV and display the first five lines of the CSV file
    convert_xlsx_to_csv(fetched_folder_name, "cars.xlsx", "cars.csv")
    display_first_five_lines_csv(fetched_folder_name, "cars.csv")
    
    # Find the top 10 most common words in the fetched text file
    find_top_10_common_words(fetched_folder_name, "warpeace.txt")
    
    #display_json_data(fetched_folder_name, "astros.json")
    display_json_data_sorted_by_craft(fetched_folder_name, "astros.json")

    # Create a histogram for the bikes.csv file
    create_histogram_for_bikes(fetched_folder_name, "bikes.csv")
    

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


######################
# Conditional Execution
######################

if __name__ == '__main__':
    main()