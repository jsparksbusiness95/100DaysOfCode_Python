num_range = range(1,101)
total_num = 0
for number in num_range:
    # number =+ total_num - Original code, left in for note-taking.
    total_num += number # Python reads l-to-r, logic is total_num + and = number; reversing statement will not work.
print(total_num)