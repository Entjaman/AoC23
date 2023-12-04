import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

res = 0
for line in lines:
    i = 0
    line = line[8:] # "remove Card 1: " etc
    winning_numbers, current_numbers = line.split('|')
    winning_numbers = "".join(winning_numbers).split() # update so each number is an element
    current_numbers = "".join(current_numbers).split() # update so each number is an element
    for current_number in current_numbers:
        if current_number in winning_numbers:
            i += 1
    res += 2**(i-1) if (i > 0) else 0
print(res)
