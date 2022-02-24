import random
import art

def game(answer, guesses):
  guess = ''
  while guesses > 0 :
    print("You have "+ str(guesses) + " attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
      return "You Got It"
    if guess > answer:
      print("Too High.")
      guesses -= 1
    if guess < answer:
      print("Too Low.")
      guesses -= 1
    if guesses > 0:
      print("Guess Again")
  return("You Ran Out Of Guesses, You Lose")
  

print(art.logo) 
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
answer = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  print(game(answer, 10))
elif difficulty == "hard":
  print(game(answer, 5))
else:
  print("Invalid Input")


