''' ITERATION 5

Module: Underwater Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline should be used in every Python analytics project we do.

Process:

In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''

#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`: This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code. 
# Did you find statistics.mean()?
# Did you find statistics.stdev()?

import statistics

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Boolean variable to indicate if the company is pet friendly
is_pet_friendly: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# Integer variable for the number of rescues at years_in_operation
has_been_rescued: int = 1 

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of strings representing SCUBA diving destinations
scuba_destinations: list = ["Bali", "Maldives", "Tubataha", "Cabo Pulmo"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# List of floats representing depths of recent dives in meters
scuba_depths_meters: list = [20.1, 32.6, 27.4, 18.3, 39.4]

#####################################
# Calculate Basic Statistics 
#   Do this BEFORE we declare the byline 
#   So the values have been calculated 
#   and are ready for use in the byline.
#####################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_score_scuba: float = min(scuba_depths_meters)  
max_score_scuba: float = max(scuba_depths_meters)  
mean_score_scuba: float = statistics.mean(scuba_depths_meters)  
stdev_score_scuba: float = statistics.stdev(scuba_depths_meters)

# note to self: I added a lot more variables than needed

#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Underwater Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Is pet friendly:            {is_pet_friendly}
Years in Operation:         {years_in_operation}
Times Rescued at Sea:       {has_been_rescued}
Skills Offered:             {skills_offered}
Places to SCUBA Dive        {scuba_destinations}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
Recent dive depths (meters):{scuba_depths_meters}
Minimum Dive Depth:         {min_score}
Maximum Dive Depth:         {max_score}
Mean Dive Depth:            {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
    
