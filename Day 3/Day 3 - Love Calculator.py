print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower1 = name1.lower()
lower2 = name2.lower()
full_string1 = lower1 + lower2

Tcount = int(full_string1.count("t"))
Rcount = int(full_string1.count("r"))
Ucount = int(full_string1.count("u"))
E1count = int(full_string1.count("e"))
Lcount = int(full_string1.count("l"))
Ocount = int(full_string1.count("o"))
Vcount = int(full_string1.count("v"))
E2count = int(full_string1.count("e"))

TrueCount = str(Tcount + Rcount + Ucount + E1count)
Lovecount = str(Lcount + Ocount + Vcount + E2count)
full_string2 = TrueCount + Lovecount
intergerstring = int (full_string2)

if (intergerstring < 10) or (intergerstring > 90):
    print(f"Your score is {intergerstring}, you go together like coke and mentos")
elif (40< intergerstring < 50):
    print(f"Your score is {intergerstring}, you are alright together")
else:
    print(f"Your score is {intergerstring}")