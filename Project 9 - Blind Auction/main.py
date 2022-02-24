from replit import clear
import art

def find_winner(bids):

  top_bid = 0
  top_key = ""
  for key in bids:
    if bids[key] > top_bid:
      top_bid = bids[key]
      top_key = key

  print("The winner is " + top_key + " with a bid of $" + str(top_bid))

print(art.logo)
bids = {}
run = "yes"
while run == "yes":
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bids[name] = int(bid)
  run =  input("Are there any other bidders? Type 'yes' or 'no'. \n")
  clear()
find_winner(bids)

