print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? ₹"))

percentage = float(input("What percentage bill would you like to give? 10, 12, or 15? "))

finalPercentage = (100 + percentage)/100

person = int(input("How many persons to split the bill? "))

payment = (totalBill/person) * finalPercentage

# roundpayment = round(payment, 2)

roundpayment = "{:.2f}".format(payment)

# print("Each person will pay: " + .2f{roundpayment}.round")

print(f"Each person will pay: {roundpayment}")
