# Import random module from Python
import random
# Test import of custom module
import my_module

rand_val = random.randint(1,10)
print(f"Your random number is: {rand_val}.")
print("\n" + my_module.quote_FotNS)


# Coin toss code
coinToss = random.randint(0,1)
if coinToss == 0:
    print("It landed on heads.")
else:
    print("It landed on tails.")
