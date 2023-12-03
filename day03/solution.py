import re

with open('./test.txt', 'r') as file:
    lines = file.readlines()

def find_indexes(matches: list[tuple[str, str]], line: str) -> list[tuple[int, int]]:
    return [(line.index(match), line.index(match) + (len(match) - 1)) for match in matches]


def calc_partnumbers(numbers: dict[list[tuple[int, int]]], values: dict[list[int]], symbols: dict[list[tuple[int, int]]]):
    res = 0
    found_val = False

    for row_number, list_number in numbers.items():
        for i, number_tuple in enumerate(list_number):
            number_start, number_end = number_tuple
            found_val = False
            try:
                for symbol_tuple in symbols[row_number - 1]: # check above
                    symbol_start, symbol_end = symbol_tuple
                    if symbol_end == number_start - 1 or symbol_start == number_end + 1 or (symbol_start >= number_start and symbol_end <= symbol_end):
                        found_val = True
                        break
            except KeyError:
                pass
            try:
                for symbol_tuple in symbols[row_number]: # check same row
                    symbol_start, symbol_end = symbol_tuple
                    if symbol_end == number_start - 1 or symbol_start == number_end + 1:
                        found_val = True
            except KeyError:
                pass
            try:
                for symbol_tuple in symbols[row_number + 1]: # check below
                    symbol_start, symbol_end = symbol_tuple
                    if symbol_end == number_start - 1 or symbol_start == number_end + 1 or (symbol_start >= number_start and symbol_end <= symbol_end):
                        found_val = True
            except KeyError:
                pass
            if found_val:
                res += values[row_number][i]
    return res
    

numbers = {}
symbols = {}
values = {}
numbers_pattern = re.compile(r"(\d+)")
symbols_pattern = re.compile(r"[&\\*#%$+@=-]")

for i, line in enumerate(lines): # find numbers and their locations in the strings
    numbers_matches = re.findall(numbers_pattern, line)
    symbols_matches = re.findall(symbols_pattern, line)

    if numbers_matches:
        numbers |= {i: find_indexes(numbers_matches, line)}
        values |= {i: [abs(int(value)) for value in numbers_matches]}

    if symbols_matches:
        symbols |= {i: find_indexes(symbols_matches, line)}

print(calc_partnumbers(numbers, values, symbols))