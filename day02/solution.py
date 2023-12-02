import re

def find_color(entry:str, color: str, limit: int) -> bool:
    match = re.search(f"(\d+) {color}", entry)
    if not match: return None, True
    if int(match.group(1)) <= limit: return int(match.group(1)), True
    return int(match.group(1)), False

with open('./input.txt', 'r') as file:
    input = file.readlines()

ids = []
min_scores = []
for i, line in enumerate(input):
    line = line[8:] # remove "game 4: " etc
    entries = line.split(';')
    overflow = False
    min_red = []
    min_green = []
    min_blue = []
    for entry in entries:
        i1, red = find_color(entry, "red", 12)
        i2, green = find_color(entry, "green", 13)
        i3, blue = find_color(entry, "blue", 14)
        if not red or not green or not blue:
            overflow = True
        if i1 is not None:
            min_red.append(i1)
        if i2 is not None:
            min_green.append(i2)
        if i3 is not None:
            min_blue.append(i3)

    min_scores += [max(min_red, default=1) * max(min_green, default=1) * max(min_blue, default=1)]

    if not overflow:
        ids.append(i+1)

print(f"part 1: {sum(set(ids))}")
print(f"part 2: {sum(min_scores)}")
