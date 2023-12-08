import re
from functools import reduce

with open('input.txt', 'r') as file:
    times, distances = file.readlines()
times = [int(x) for x in times[5:].split()] # remove excess "Time:" and get values
times_p2 = [int("".join([str(x) for x in times]))]
distances = [int(x) for x in distances[9:].split()] # remove excess "Distance:" and get values
distances_p2 = [int("".join([str(x) for x in distances]))]
print(times_p2)
print(distances_p2)
traveled = [[map(lambda x, y: x * y, [*range(time + 1)], [*range(time + 1)][::-1])] for time in times]
traveled_p2 = [[map(lambda x, y: x * y, [*range(time + 1)], [*range(time + 1)][::-1])] for time in times_p2]
res = []
#for i, travel in enumerate(traveled):
for i, travel in enumerate(traveled_p2):
    count = 0
    for x in travel[0]:
        if x > distances_p2[i]:
            count += 1
    res.append(count)
print(f"p1: {reduce(lambda x, y: x*y, res)}")
