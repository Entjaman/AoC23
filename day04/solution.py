import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

# part 1
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

# part 2
def part2(lines: list[str]) -> int:
    dictionary = dict((key+1, 0) for key in range(len(lines)))
    for i, line in enumerate(lines, start=1):
        line = line[8:] # "remove Card 1: " etc
        winning_numbers, current_numbers = line.split('|')
        winning_numbers = "".join(winning_numbers).split() # update so each number is an element
        current_numbers = "".join(current_numbers).split() # update so each number is an element
        for current_number in current_numbers:
            if current_number in winning_numbers:
                dictionary[i] += 1

    def count_cards(idx, depth=0):
        score = dictionary[idx+1]
        if score == 0:
            return 1
        res = 1
        for i in range(score):
            res += count_cards(idx + i + 1, depth+1)
        return res
    return sum(count_cards(i) for i in range(len(dictionary)))

p2 = part2(lines)
print(p2)
