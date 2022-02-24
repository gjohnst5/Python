import random
import art
import replit

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rand_card = random.choice(cards)
  return rand_card

def calculate_score(hand):
  if sum(hand) > 21 and 11 in hand:
    hand.remove(11)
    hand.append(1)
  if len(hand) == 2 and sum(hand) == 21:
    return 0
  else:
    return sum(hand)

def compare(comp_score , user_score):
  if comp_score == user_score:
    return "The Game is a Draw"
  elif comp_score == 0:
    return "You Lose, the Computer has Blackjack"
  elif user_score == 0:
    return "You Win, You have Blackjack"
  elif user_score > 21:
    return "You Lose, You Went Over"
  elif comp_score > 21:
    return "You Win, the Computer Went Over"
  elif user_score > comp_score:
    return "You Win"
  else:
    return  "You Lose"

def blackjack():
  game_over = False
  user_cards = []
  computer_cards = []

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(" Your cards: " + str(user_cards) + ", current score: " + str(user_score))
    print(" Computer's first card: "+ str(computer_cards[0]))

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      deal = input("Type 'yes' to get another card, type 'no' to pass: ")
      if deal == "yes":
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("Your final hand: " + str(user_cards) + ", final score: " + str(user_score))
  print("Computer's final hand: " + str(computer_cards) + ", final score: " + str(computer_score))
  print(compare(computer_score, user_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  replit.clear()
  print(art.logo)
  blackjack()