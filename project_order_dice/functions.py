import random
import yaml
import os
import datetime


# Function to exclude the names of people who are not present.
def exclude_enter_names():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "config.yaml")
    with open(file_path, "r") as config:
        data = yaml.safe_load(config)
        filtered_names = [person["name"] for person in data["team_members"] if not person["is_away"]]

        today = datetime.date.today()
        weekday = today.isoweekday()

    # Check weekdays
    try:
        if weekday == 1:
            monday_names = data.get("Monday", [])
            for names in monday_names:
                filtered_names = [name for name in filtered_names if name not in names.get("names", [])]
        elif weekday == 2:
            tuesday_names = data.get("Tuesday", [])
            for names in tuesday_names:
                filtered_names = [name for name in filtered_names if name not in names.get("names", [])]
        elif weekday == 3:
            wednesday_names = data.get("Wednesday", [])
            for names in wednesday_names:
                filtered_names = [name for name in filtered_names if name not in names.get("names", [])]
        elif weekday == 4:
            thursday_names = data.get("Thursday", [])
            for names in thursday_names:
                filtered_names = [name for name in filtered_names if name not in names.get("names", [])]
        elif weekday == 5:
            friday_names = data.get("Friday", [])
            for names in friday_names:
                filtered_names = [name for name in filtered_names if name not in names.get("names", [])]
    except TypeError:
        pass

        # Check vacation
        for period in data["vacation"]:
            try:
                start_date = datetime.datetime.strptime(str(period["start_date"]), "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(str(period["end_date"]), "%Y-%m-%d").date()

                if start_date <= today <= end_date:
                    filtered_names = [name for name in filtered_names if name not in period["name"]]
            except ValueError:
                continue

    # Exclude names
    while True:
        try:
            not_present = input("Who is not present? :")
            if not_present in filtered_names:
                filtered_names.remove(not_present)
            elif not_present == "":
                break
            elif not_present not in filtered_names:
                raise ValueError
        except ValueError:
            print("This name is not in the List!\n Enter a name from the following list : " + ", ".join(filtered_names))

    return filtered_names


# Generate the speaking order
def generate_list(filtered_names):
    # generate the random order
    name_star = random.choice(filtered_names)

    for name in random.sample(filtered_names, len(filtered_names)):
        if name == name_star:
            print("*", name)
        else:
            print(name)


def read_away_yaml():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "config.yaml")
    with open(file_path, "r") as config:
        data = yaml.safe_load(config)
        return data
