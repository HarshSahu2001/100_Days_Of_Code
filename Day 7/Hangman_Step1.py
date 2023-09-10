#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[chosen_index]
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter:\n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
times = 0
for letter in chosen_word:
    if letter == guess:
        times += 1
print(times)
