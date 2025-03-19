# Minor formatting adjustments made.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
# Do not put "%" in input
tip = int(input("What percentage tip would you like to give? 10%, 12%, 15%, etc.\n"))
people = int(input("How many people to split the bill?\n"))

# Portion is the bill plus the tip (divided by the total bill) then divide by the number of people.
portion = ((bill + (bill / tip)) / people)
# f-string to print the portion variable, rounded to the second decimal.
print(f"Everyone needs to pay ${round(portion, 2)}.")
