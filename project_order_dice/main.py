#!/usr/bin/env python3
import functions
from functions import read_away_yaml
print("-------------------------Daily Speaking Order Dice--------------------- ")
print("Below you can enter the names of the team members who are not present")
print("If all members are present simply press return")
data = read_away_yaml()
# Function to build the list of participating names
filtered_names = functions.build_todays_participants(data)

# Function to manually exclude people who are not available at the current day
functions.manuel_exclude(filtered_names)

# Generate the speaking order.
print("The randomly generated order is: ")
functions.generate_list(filtered_names)
