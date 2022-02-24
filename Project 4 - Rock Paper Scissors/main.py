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

#Write your code below this line 👇
import random
rps = [rock, paper, scissors]
random_num = random.randint(0, len(rps)-1)

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
int_choice = int(choice)
user_choice = rps[int_choice]
print(user_choice)


print("Computer chose: ")
computer_choice = rps[random_num]
print(computer_choice)

if(int_choice == random_num):
  print("You Tied")
elif(int_choice == 0):
  if(random_num == 2):
    print("You Win")
  else:
    print("You Lose")
elif(int_choice == 1):
  if(random_num == 0):
    print("You Win")
  else:
    print("You Lose")
elif(int_choice == 2):
  if(random_num == 1):
    print("You Win")
  else:
    print("You Lose")
else:
  print("Invalid Number You Lose")


