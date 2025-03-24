# Modified original problem to instead check for age first, then height.
# This is done so that customers over 18 can ride the ride even at a short height.

print("Welcome to the rollercoaster!")
custAge = int(input("What is your age?\n"))
custHeight = int(input("What is your height in cm?\n"))

if custAge < 12:
    if custHeight >= 120:
        print("You can ride the rollercoaster. Please insert $5.")
    else:
        print("Sorry you have to grow taller before you can ride.")
elif 12 <= custAge < 18:
    if custHeight >= 120:
        print("You can ride the rollercoaster. Please insert $7.")
    else:
        print("Sorry you have to grow taller before you can ride.")
else:
    print("You can ride the rollercoaster. Please insert $12.")
