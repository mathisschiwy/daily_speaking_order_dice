import random
names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
all_names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
# Function to exclude the names of people who are not present.
def enter_names(names):
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
    for name in random.sample(names, len(names)):
        print(name)