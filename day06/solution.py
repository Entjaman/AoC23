import re
from functools import reduce

with open('input.txt', 'r') as file:
    times, distances = file.readlines()
times = [int(x) for x in times[5:].split()] # remove excess "Time:" and get values
distances = [int(x) for x in distances[9:].split()] # remove excess "Distance:" and get values
traveled = [[map(lambda x, y: x * y, [*range(time + 1)], [*range(time + 1)][::-1])] for time in times]
res = []
for i, travel in enumerate(traveled):
    count = 0
    for x in travel[0]:
        if x > distances[i]:
            count += 1
    res.append(count)
print(f"p1: {reduce(lambda x, y: x*y, res)}")