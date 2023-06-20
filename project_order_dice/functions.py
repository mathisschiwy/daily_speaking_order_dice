import random
import yaml
import os
names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
all_names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
# Function to exclude the names of people who are not present.
def exclude_enter_names(names):
    while True:
        try:
            not_present = input("Who is not present? :")
            if not_present != "":
                names.remove(not_present)
            elif not_present == "":
                break
        except:
            print("This name is not in the List!\n Enter a name from the following list : "+", ".join(all_names))

# Generate the speaking order.
def generate_list(names):

 #Open yaml file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "Config/away.yaml")

    with open(file_path, "r") as config:
        data = yaml.safe_load(config)

#Filter the List
        filtered_names = [person["name"] for person in data if not person.get("is_away")]

#generate the random order
    name_star = random.choice(filtered_names)
    for name in random.sample(filtered_names, len(filtered_names)):
        if name == name_star:
            print("*", name)
        else:
            print(name)
    return filtered_names
