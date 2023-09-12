# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Function with no parameter
# def greet():
#     print("Hey There")
#     print("Greetings of the day!")
#     print("Have a Good Day!")

# greet()

#Function with input parameter
# def function_with_name(name):
#     print(f"Hey There, {name}")
#     print(f"Greetings of the day {name}!")
#     print(f"Have a Good Day {name}!")

# function_with_name("Harsh")


#Function with 2 parameters
# def greet_with(Name, location):
#     print(f"Hello {Name} from {location}")
#     print(f"{Name} is from {location}")

# greet_with ("Harsh", "Biaora")

#Function with keyword Arguement
def greet(Name, location):
  print(f"Hey {Name}!!")
  print(f"Are you from {location}?")

greet(location = "Biaora", Name = "Harsh")
