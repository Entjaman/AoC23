import re
from collections import Counter
from functools import cmp_to_key

with open('input.txt', 'r') as file:
    lines = file.readlines()

types = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8,
         "7":7,"6":6, "5":5, "4":4, "3":3, "2":2}
labels = {"five_kind":8, "four_kind": 7, "full_house": 6, "three_kind": 5,
          "two_pair":4, "one_pair":3, "two_of_a_kind": 2, "high_card": 1}

# helper function
def get_type(hand):
    counterObj = Counter()
    for label in hand:
        counterObj[label] += 1
    items = counterObj.items()
    curr_types = [type[0] for type in items]
    commons = counterObj.most_common(2)
    most_common = commons[0]
    try:
        least_common = commons[1]
    except IndexError:
        pass
    instances = most_common[1]
    match instances:
        case 1:
            return [(hand, labels["high_card"], instances)]
        case 2:
            if least_common[1] == 2:
                return [(hand, labels["two_pair"], instances)]
            return [(hand, labels["two_of_a_kind"], instances)]
        case 3:
            if least_common[1] == 2:
                return [(hand, labels["full_house"], instances)]
            return [(hand, labels["three_kind"], instances)]
        case 4:
            return [(hand, labels["four_kind"], instances)]
        case 5:
            return [(hand, labels["five_kind"], instances)]


def custom_sort(hand1, hand2):
    cmp = hand1[1] - hand2[1]
    if cmp != 0:
        return cmp
    for i in range(5):
        cmp = types[hand1[0][i]] - types[hand2[0][i]]
        if cmp != 0:
            return cmp
    return 0

hands = []
# setup
for line in lines:
    hand, bid = line.split()
    hands.append((hand, bid))
# for each tuple in strengths: ('current hand', label', 'instances', 'bid value')
results = [get_type(hand[0])[0] + (int(hand[1]),) for hand in hands]
results.sort(key=cmp_to_key(custom_sort))
print(f"p1: {sum([rank * bid[3] for rank, bid in enumerate(results, start=1)])}")
