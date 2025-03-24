# Modified original problem to instead check for age first, then height.
# This is done so that customers over 18 can ride the ride even at a short height.
# Modified code to now increment ticket price and add value of photo to final ticket price

print("Welcome to the rollercoaster!")
custAge = int(input("What is your age?\n"))
custHeight = int(input("What is your height in cm?\n"))
custTicket = 0
wantsPhoto = "n"

if custAge < 12:
    if custHeight >= 120:
        custTicket = 5
        wantsPhoto = input("You can ride the rollercoaster. Would you like a photo (Y/N)?\n")
        if wantsPhoto == "y":
            custTicket += 3
            print(f"Your total is ${custTicket}.")
        else:
            print(f"Your total is ${custTicket}.")
    else:
        print("Sorry you have to grow taller before you can ride.")
elif 12 <= custAge < 18:
    if custHeight >= 120:
        custTicket = 7
        wantsPhoto = input("You can ride the rollercoaster. Would you like a photo (Y/N)?\n")
        if wantsPhoto == "y":
            custTicket += 3
            print(f"Your total is ${custTicket}.")
        else:
            print(f"Your total is ${custTicket}.")
    else:
        print("Sorry you have to grow taller before you can ride.")
else:
    custTicket = 12
    wantsPhoto = input("You can ride the rollercoaster. Would you like a photo (Y/N)?\n")
    if wantsPhoto == "y":
        custTicket += 3
        print(f"Your total is ${custTicket}.")
    else:
        print(f"Your total is ${custTicket}.")