import re
from typing import List


def process_block(source_values: List[int], values: List[int]) -> List[int]:
    destination_values = [-1]*len(source_values)
    for i in range(0, len(values), 3):
        destination = values[i]
        source = values[i + 1]
        r = values[i + 2]

        for j, source_value in enumerate(source_values):
            if source <= source_value <= source + (r - 1):
                destination_values[j] = destination + (source_value - source)

    for i, destination_value in enumerate(destination_values):
        if destination_value == -1:
            destination_values[i] = source_values[i]

    return destination_values


if __name__ == '__main__':

    # NOTE: This is the first implementation of the solution, which is not optimized.
    #  see the part two for a more optimized solution

    with open('input.txt', 'r') as f:
        first_line = f.readline()
        maps = f.read()

    source_values = list(map(lambda x: int(x), re.findall(r'\s*(\d+)\s*', first_line)))

    maps = maps.split('\n\n')
    for raw_map in maps:
        map_values = list(map(lambda x: int(x), re.findall(r'\s*(\d+)\s*', raw_map)))
        source_values = process_block(source_values, map_values)

    print(min(source_values))


