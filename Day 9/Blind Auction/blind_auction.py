from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_records):
  highest_bid = 0
  winnner = ""
  for bidder in bidding_records:
    bid_amount = bidding_records[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winnner = bidder
  print(f"Highest Bid is {highest_bid} from {bidder}")
  
while bidding_finished == False:
  name = input("Enter Your Name: ")
  price = int(input("Enter The Price: $"))
  bids[name] = price
  should_continue = input("Do You Want To Add More Bids? Say Yes or No?" ).lower()
  if should_continue == "yes":
    clear()
  else:
    bidding_finished = True
    highest_bidder(bids)
