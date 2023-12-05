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

# map = {
#     "seed": [],
#     "soil": [],
#     "fertilizer": [],
#     "water": [],
#     "light": [],
#     "temperature": [],
#     "humidity": [],
#     "location": []
# }

items = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
#mapping = [[], [], [], [], [], [], [], []]

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

# begin mapping source to destination
for i, type in enumerate(types.values()):
    for row in type:
        destination = row[0] # destination range start
        source = row[1] # source range start
        length = row[2] # range length
        for j in range(length):
            map_table[i].append((source +  j, destination + j)) # source -> destination mapping
    source_values = [val[0] for val in map_table[i]] # all source values
    destination_values = [val[1] for val in map_table[i]] # all destination values
    temp = max(source_values) if max(source_values) > max(destination_values) else max(destination_values)
    if temp > len(map_table[i]):
        for k in range(temp):
            if k not in source_values:
                map_table[i].append((k, k))

def lookup(target):
    for table in map_table:
        for source, destination in table:
            if target == source:
                return destination

location = []
for seed in seeds:
    temp = seed
    print(temp)
    for i in enumerate(map_table):
        temp = lookup(temp)
        print(temp)
    location.append(temp)
print(min(location))

#print(map_table)
# begin constructing table
# for i, list in enumerate(map_table):
#     for source, destination in list:
#         if source in mapping[i] and i == 0:
#             mapping[i+1].append({source: destination})
#         else:
#             mapping[i+1].append({source: source})
# for map in mapping:
#     print(map)
#     print()