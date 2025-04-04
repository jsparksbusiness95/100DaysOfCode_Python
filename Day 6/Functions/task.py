def test():
    temp_name = input("Hello, user! What is your name?\n")
    begin_coding = input(f"Hello {temp_name}! Welcome to Python! Are you ready to get started on your code adventure? y/n\n")
    begin_coding = begin_coding.lower()
    if begin_coding == "y":
        print("Great! Let's being:\n")
    elif begin_coding == "n":
        print("Too bad. See you next time!\n")
    else:
        print("Oops. I didn't recognize that. Let's try that again later.\n")

test()

# Reborg's World Practice Exercise 1:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#
# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# Reborg's World Practice Exercise 2:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#
# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# move()
# jump()
# move()
# jump()
# move()
# jump()
# move()
# jump()
# move()
# jump()
# move()
# jump()

# Reborg's World Practice Exercise 3:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#
# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() == False: # while at_goal() := True: # while not at_goal():
#     move()
#     jump()

# Reborg's World Practice Exercise 4:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#
# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() == False:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         jump()

# Reborg's World Practice Exercise 5:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#
# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear() == True:
#         move()
#     turn_left()
#
# while at_goal() == False:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         jump()

# Reborg's World Practice Exercise 6 - Maze:
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Answer:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def move_north():
#     while is_facing_north() == False:
#         turn_left()
#     move()
#
# while at_goal() == False:
#     if right_is_clear() == True:
#         if front_is_clear() == True:
#             move_north()
#         else:
#             turn_right()
#             move()
#     elif wall_on_right() == True:
#         if front_is_clear():
#             move()
#         else:
#             turn_left()