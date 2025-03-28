fb_game_range = range(1, 101)

# for num in fb_game_range: ---- Bad original code
#     if num % 3:
#         print("Fizz")
#     elif num % 5:
#         num = "Buzz"
#     elif num % 3 and num % 5:
#         num = "FizzBuzz"

# In your original code, the elif num % 5 condition would always be True when num % 3 is not True
# (i.e., when num is not cleanly divisible by 3), because any non-zero number is considered True
# in a boolean context. This would result in the output only containing "Buzz" or "FizzBuzz", but
# never just "Fizz".
#
# By separating the conditions for divisibility by 3, 5, and both, you can ensure that the correct
# output is printed for each number in the range.


for num in fb_game_range:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)