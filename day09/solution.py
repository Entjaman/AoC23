from itertools import pairwise

with open('input.txt', 'r') as file:
    lines = file.readlines()

sequences = []
for line in lines:
    sequences.append([int(num) for num in line.split()])

i = 0
for seq in sequences:
    diffs = seq
    history = [seq]
    while True:
        diffs = curr = [y-x for (x,y) in pairwise(diffs)]
        history.append(diffs)
        if all(val == 0 for val in diffs):
            break