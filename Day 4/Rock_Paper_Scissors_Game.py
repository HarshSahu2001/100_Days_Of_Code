import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

User_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: \n"))

if User_input >= 3 or User_input <= 0:
    print("You Chose an invalid number, Hence you Lose")
else:
    Outcomes = [rock, paper, scissors]
    print(Outcomes[User_input])

    Computer_choice = random.randint(0, 2)
    print(f"Computer Chose {Computer_choice}")
    print(Outcomes[Computer_choice])

    if User_input == 0 and Computer_choice == 2:
        print("You Win!")
    elif User_input == 2 and Computer_choice == 0:
        print("You Lose")
    elif Computer_choice > User_input:
        print("You Lose")
    elif Computer_choice < User_input:
        print("You Win")
    elif User_input == Computer_choice:
        print("It's a Draw")
