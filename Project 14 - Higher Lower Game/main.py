import random
import art
import game_data
import replit

def format_output(data):
  return data["name"] + ", a " + data["description"] + ", from "+ data["country"] + "."

score = 0
run = True
winner = ""
guess = ""
print(art.logo)
game_data_1 = random.choice(game_data.data)

while run:
  
  game_data_2 = random.choice(game_data.data)
  while game_data_1 == game_data_2:
    game_data_2 = random.choice(game_data.data)

  print("Compare A: " + format_output(game_data_1))
  num_A = game_data_1["follower_count"]
  print(art.vs)
  print("Against B: " + format_output(game_data_2))
  num_B = game_data_2["follower_count"]

  if num_A > num_B:
    winner = "a"
  else:
    winner = "b"
    

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  replit.clear()
  print(art.logo)
  if guess == winner:
    score += 1
    game_data_1 = game_data_2
    print("You're right! Current score: " + str(score))
  else:
    run = False
    print("Sorry, that's wrong. Final score: " + str(score))