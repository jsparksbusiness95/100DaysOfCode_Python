# Slight edits to code, added extra sauce and tip calculation to apply old concepts.
# Code does not pass internal checker, verified code works as intended w/ modifications.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extra cheese? Y or N:\n")
extra_sauce = input("Do you want extra sauce? Y or N:\n")
include_tip = input("Would you like to add a tip? Y/N\n")
bill_tip = int(input("What percent gratuity would you like to include? (10, 15, 20)\n"))
bill_before_tip = 0

# Pizza Size Prices
if size == "s":
    bill_before_tip = 15
elif size == "m":
    bill_before_tip = 20
elif size == "l":
    bill_before_tip = 25
else:
    print("Error: Invalid Input. Please run again.")

# Pepperoni Prices
if pepperoni == "y":
    if size == "s":
        bill_before_tip += 2
    else:
        bill_before_tip += 3

# Extra Cheese Prices
if extra_cheese == "y":
    bill_before_tip += 1

# Extra Sauce Prices
if extra_sauce == "y":
        bill_before_tip += 1

# Debugger: Verify size loop works correctly, uncomment as needed.
# print(f"Your total is {bill_before_tip}")

# Bill calculation for tip (if added).
if include_tip == "y":
    tip_percent = round(bill_tip / 100, 2)
    final_bill = (round(bill_before_tip * tip_percent + bill_before_tip, 2))
    print(f"Your total is: ${final_bill}")
else:
    final_bill = bill_before_tip
    print(f"Your total is: ${final_bill}")
