#!/usr/bin/env python3
import functions
print("-------------------------Daily Speaking Order Dice--------------------- ")
print("Below you can enter the names of the team members who are not present")
print("If all members are present simply press return")

# Function to exclude the names of people who are not present.
filtered_names = functions.exclude_enter_names()

# Generate the speaking order.
print("The randomly generated order is: ")
functions.generate_list(filtered_names)
