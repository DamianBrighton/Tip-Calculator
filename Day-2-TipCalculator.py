# Day 2: Tip calculator

print("Welcome to the Tip calculator")
#Creating variables to store the inputs into
amount = float(input("What is your total bill?\n"))
tip_amount = int(input("How much would you like to tip? 10, 12, or 15?\n"))
people= int(input("How many people would you like to split the bill between?\n"))
#formula for calculating the tip
tot_tip= tip_amount/100
tot_tip_amount = amount * tot_tip
tot_amount = amount + tot_tip_amount
tot_person = tot_amount / people
total = round(tot_person, 2)
total = "{:.2f}".format(tot_person)

#Print statement
print(f"Each person should pay R{total}.")