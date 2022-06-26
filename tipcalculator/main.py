#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#grab data inputs
print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#change to Integers
bill_as_float = float(bill)
people_as_int = int(people)                 
percent_as_int = int(percent)

#Do some Mathing
total = (bill_as_float * (percent_as_int/100) + bill_as_float)
split = (total / people_as_int)

#Format to always have 2 places after decimal
answer = "{:.2f}".format(split)

#Print it with an fString
print(f"Each person should pay: ${answer}")