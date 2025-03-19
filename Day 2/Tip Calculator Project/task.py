# Minor formatting adjustments made.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
# Do not put "%" in input
tip = int(input("What percentage tip would you like to give? 10%, 12%, 15%, etc. Please do not include the % symbol.\n"))
people = int(input("How many people to split the bill?\n"))

# My logic
tip_percent = round(tip / 100, 2)
finalBill = ((round(bill * tip_percent + bill,2)) / people)

# f-string to print the portion variable, rounded to the second decimal.
print(f"Everyone needs to pay: ${round(finalBill, 2)}.")
