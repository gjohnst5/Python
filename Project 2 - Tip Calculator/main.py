#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

after_tip = float(total_bill) + round((float(total_bill) * (float(tip)/100)),2)
answer = round(after_tip / float(people), 2)

print("Each person should pay: $" + str(answer))