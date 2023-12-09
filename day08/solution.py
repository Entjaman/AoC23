with open('input.txt', 'r') as file:
    lines = file.readlines()

instructions = lines[0].strip()
paths = {}

#setup
for line in lines[2:]:
    print(line)
    key, tuple = line.split(' = ')
    L, R = tuple.strip("()\n").split(', ')
    paths[key] = (L, R)

# calc
found_zzz = False
i = 0
curr_node = "AAA"
while not found_zzz:
    for instruction in instructions:
        curr_node = paths[curr_node][0] if instruction == 'L' else paths[curr_node][1]
        i += 1
        if curr_node == "ZZZ":
            found_zzz = True
            break
print(f"p1: {i}")
        