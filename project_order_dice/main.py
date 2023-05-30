import random

names = ["Hannes", "Jessica", "Henning", "Mathis", "Sarah", "Steffen"]
not_present = []

while True:
    not_present = input("Enter the names : ")
    if not_present != "":
        names.remove(not_present)
    elif not_present == "":
        break

for name in random.sample(names, len(names)):
    print(name)

