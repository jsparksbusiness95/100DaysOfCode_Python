print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n\n")
travel_foot = input("There is a fork at the road. Will you go left or right?\n").lower()

# Which direction to go?
if travel_foot == "left":
    # Swim or take the boat?
    travel_water = input("You come across a large body of water. Will you swim across or wait for a boat?\n")
    if travel_water == "wait":
        print("The ferryman has finally arrived. He'll take you to the Isle of Treasure!\n")
        # What door to take?
        select_door = input(
            "You've come to a temple with three doors--one red, one blue, and one yellow. Which door do you go through?\n").lower()
        if select_door == "red":
            print("You've entered the Tomb of Flames! The flames engulf you before you pass out. Upon awakening, you find that it was all a dream.\n\nGAME OVER!")
        elif select_door == "blue":
            print("You've entered the Tomb of Sorrows! You are suddenly overwhelmed by feelings of sadness and decided to go home to call your mom.\n\nGAME OVER!")
        elif select_door == "yellow":
            print("You've entered the Tomb of Treasure! It's less of a tomb and more a closet. Either way, you get a single gold coin for your troubles.\n\nYOU WIN!")
        else:
            print("The temple has sensed you don't intend to go through any of the doors. In an instant, you find yourself teleported home for being a bad sport.\n\nGAME OVER!")
    elif travel_water == "swim":
        print("You don't know how to swim. Fortunately a fisherman saves you, but in exchange you have to help him with fishing for the day.\n\nGAME OVER!")
    else:
        print("The sea itself has taken a liking to you--probably cause you didn't play by the rules. You rebel scum. Either way, you've now been made a fish and cannot go on with your adventure.\n\nGAME OVER!")
else:
    print("There was no other path. Confused, you give up and go home.\n\nGAME OVER!")