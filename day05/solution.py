import re

with open('./test.txt', 'r') as file:
    input = file.read()

types = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}

map_table = [[], [], [], [], [], [], []]

map = {
    "seed": [],
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": [],
    "location": []
}

#map = [[], [], [], [], [], [], [], []]

seeds = [int(x) for x in input.split('\n')[0][7:].split()] # get first line and remove "seeds: " and then get numbers

# parse textfile
for type in types:
    pattern = re.compile(fr"{type} map:\n(.*?)\n\n", re.DOTALL)
    match = pattern.search(input)
    if not match:
        raise LookupError(f"Couldn't find values to {type}")
    match = match.group(1).split('\n')
    for line in match:
        types[type].append([int(val) for val in line.split()])
print(types)

res = []
# begin mapping source to destination
for i, type in enumerate(types.values()):
    for row in type:
        destination = row[0] # destination range start
        source = row[1] # source range start
        length = row[2] # range length
        for j in range(length):
            map_table[i].append((source +  j, destination + j)) # source -> destination mapping

# begin constructing table
for list in map_table:
    for source, destination in list:
        if source in map[0]:
            pass