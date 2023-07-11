import random
import yaml
import os
import datetime


def read_away_yaml():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "config.yaml")
    with open(file_path, "r") as config:
        data = yaml.safe_load(config)
        return data


# Function to exclude the names of people who are not present.
def build_todays_participants(data):
    """
    Build the list of participating names for today/now, taking into account
    the configuration and asking the user interactively for people who are
    not there today.

    :return:
    """

    todays_participants = list()

    team_members_info = data["team_members"]

    for team_member_info in team_members_info:
        if not team_member_info["is_away"]:
            todays_participants.append(team_member_info["name"])

    today = datetime.date.today()
    weekday = today.isoweekday()

    # names of participants for current_day
    current_day_excluded_names = None

    # Check weekdays
    if weekday == 1:
        current_day_excluded_names = data.get("Monday", [])
    elif weekday == 2:
        current_day_excluded_names = data.get("Tuesday", [])
    elif weekday == 3:
        current_day_excluded_names = data.get("Wednesday", [])
    elif weekday == 4:
        current_day_excluded_names = data.get("Thursday", [])
    elif weekday == 5:
        current_day_excluded_names = data.get("Friday", [])
    else:
        print("No work day.")

    for name in todays_participants:
        if name in current_day_excluded_names:
            todays_participants.remove(name)

    # Check vacation
    for period in data["vacation"]:
        # If any of the fields is empty/none we skip this period entry
        if period["start_date"] is None:
            continue
        if period["end_date"] is None:
            continue
        if period["name"] is None:
            continue
        start_date = datetime.datetime.strptime(str(period["start_date"]), "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(str(period["end_date"]), "%Y-%m-%d").date()

        if start_date <= today <= end_date:
            for name in todays_participants:
                if name in period["name"]:
                    todays_participants.remove(name)

    return todays_participants


# Exclude names interactively
def manual_exclude(todays_participants):
    while True:
        try:
            not_present = input("Who is not present? :")
            if not_present in todays_participants:
                todays_participants.remove(not_present)
            elif not_present == "":
                break
            elif not_present not in todays_participants:
                raise ValueError
        except ValueError:
            print("This name is not in the List!\n Enter a name from the following list : " + ", ".join(
                todays_participants))

    return todays_participants


# Generate the speaking order
def generate_list(todays_participants):
    """
    generate the random order of all names given as input,
    and mark the Screening name with a star.

    :param todays_participants:
    :return:
    """
    name_star = random.choice(todays_participants)

    for name in random.sample(todays_participants, len(todays_participants)):
        if name == name_star:
            print("*", name)
        else:
            print(name)
