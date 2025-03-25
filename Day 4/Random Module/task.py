# Import random module from Python
import random
# Test import of custom module
import my_module

rand_int = random.randint(1,10)
rand_float = random.random()
rand_float_u = random.uniform(1,10)
print(f"Your random integer is: {rand_int}.\n")
print(f"Your random float is: {rand_float}.\n")
print(f"Your random uniform float is: {rand_float_u}.\n")
print(my_module.quote_FotNS + "\n")


# Coin toss code
coinToss = random.randint(0,1)
if coinToss == 0:
    print("It landed on heads.")
else:
    print("It landed on tails.")
