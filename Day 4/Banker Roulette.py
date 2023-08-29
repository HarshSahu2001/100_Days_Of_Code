import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

Choice = random.choice(names)
print(Choice + " is going to buy the meal today!")