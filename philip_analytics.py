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
import utils_philip


######################
# Declare Global Variables
######################

fetched_folder_name = "fetched"

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

 # Extract words from the text file and count occurrences of the most common 10 words
def count_words_in_text_file(folder_name:str, filename:str) -> None:
    '''
    This function counts the occurrences of the most common 10 words in a text file.
    '''
    # Read the text file
    with open(f'{folder_name}/{filename}', 'r') as file:
        text = file.read()
    
    # Split the text into words
    words = text.split()
    
    # Count the occurrences of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort the words by their counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print the most common 10 words
    for word, count in sorted_word_counts[:10]:
        print(f'{word}: {count}')

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
    # TODO: Change this to use your module function and uncomment
    case_project_setup.create_folders_from_list([fetched_folder_name])

    # Web locations of different types of data to fetch
    # TODO: Optional find different urls for 4 different types of data                               
    excel_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx' 
    json_url:str = 'http://api.open-notify.org/astros.json'
    txt_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/romeo.txt'
    csv_url:str = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    # Fetch data files - provide the fetched file names
    fetch_excel_file(fetched_folder_name, "feedback.xlsx", excel_url)
    fetch_json_file(fetched_folder_name, "astros.json", json_url)
    fetch_txt_file(fetched_folder_name, "romeo.txt", txt_url)
    fetch_csv_file(fetched_folder_name, "2020_happiness.csv", csv_url)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


######################
# Conditional Execution
######################

if __name__ == '__main__':
    main()