import re

def find_color(entry:str, color: str, limit: int) -> bool:
    match = re.search(f"(\d+) {color}", entry)
    if not match: return True
    if int(match.group(1)) <= limit: return True
    return False

with open('./input.txt', 'r') as file:
    input = file.readlines()

ids = []
for i, line in enumerate(input):
    line = line[8:] # remove "game 4: " etc
    entries = line.split(';')
    overflow = False
    for entry in entries:
        red = find_color(entry, "red", 12)
        green = find_color(entry, "green", 13)
        blue = find_color(entry, "blue", 14)
        if not red or not green or not blue:
            overflow = True 
    if not overflow:
        ids.append(i+1)

print(f"part 1: {sum(set(ids))}")
