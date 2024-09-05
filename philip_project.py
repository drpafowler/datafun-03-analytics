'''
This is the main file for the module 2 project. It will be used to create folders for the project.
'''
# Importing the necessary libraries
import pathlib
import time
import utils_philip

############################################################################################################
# Declare the global variables

# The path to the project folder
project_path = pathlib.Path.cwd() 

# The path to the data folder
data_path = project_path / 'data'

# create the data folder
data_path.mkdir(exist_ok=True)


############################################################################################################
# Create the folders for a range of years

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    This function creates folders for a range of years.
    '''
    
    for year in range(start_year, end_year + 1):
        year_folder = data_path / str(year)
        year_folder.mkdir(exist_ok=True)
        print(f"Created folder for {year}")
        time.sleep(1)

############################################################################################################
# Create folders from a list

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
    '''
    This function creates folders from a list.
    '''
    
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        folder_path = data_path / folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder for {folder_name}")
        time.sleep(1)

############################################################################################################
# Create prefixed folders

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    This function creates folders with a prefix.
    '''
    
    for folder in folder_list:
        folder_path = data_path / f"{prefix}-{folder}"
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder for {folder}")
        time.sleep(1)

############################################################################################################
# Create a folder periodically

def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
    '''
    This function creates folders periodically.
    '''

    for i in range(folder_count):
        folder_path = data_path / f"folder_{i}"
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder {i}")
        time.sleep(duration_seconds)

############################################################################################################
# Main function

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")
    
    # print the byline
    print(f"Byline: {utils_philip.get_byline()}")

    # call the create_folders_for_range function
    create_folders_for_range(start_year=2020, end_year=2023)

    # call the create_folders_from_list function
    create_folders_from_list(folder_list=['csv', 'excel', 'json'])

    # call the create_prefixed_folders function
    create_prefixed_folders(folder_list=['csv', 'excel', 'json'], prefix='data')

    #call the create_folders_periodically function using while loop
    create_folders_periodically(folder_count=3, duration_seconds=5)

    #Define a list of regions and create folders for each region
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"
    ]
    create_folders_from_list(folder_list=regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

############################################################################################################
# Conditional Execution

if __name__ == '__main__':
    main()
