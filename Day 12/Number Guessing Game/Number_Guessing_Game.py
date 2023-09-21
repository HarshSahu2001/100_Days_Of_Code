#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(Guess, Answer, turns):
  if Guess > Answer:
    print("Too high.")
    return turns - 1
  elif Guess < Answer:
    print("Too Low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {Answer}.")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
  if difficulty == "Easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    

def play_game():
  print(logo)
  print("Welcome To The Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  Answer = randint(1,100)
  # print(f"Psst, Correct Answer is {Answer}")

  turns = set_difficulty()
  
  Guess = 0
  while Guess != Answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    Guess = int(input("Guess a number: "))
    turns = check_answer(Guess, Answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif Guess != Answer:
      print("Guess Again")

play_game()