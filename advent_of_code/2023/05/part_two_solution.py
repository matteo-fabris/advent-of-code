import re
from typing import List


def get_intersected_first_last(f1: int, l1: int, target_f: int, target_l: int):
    """
    Helper function to get information
    about the overlap of two intervals
    :param f1: first value of interval 1
    :param l1: last value of interval 1
    :param target_f: first value of target interval
    :param target_l: last value of target interval
    :return: tuple of 6 values:
        - non_intersected_before_first (or -1 if not present)
        - non_intersected_before_last (or -1 if not present)
        - intersected_first (or -1 if not present)
        - intersected_last (or -1 if not present)
        - non_intersected_after_first (or -1 if not present)
        - non_intersected_after_last (or -1 if not present)
    """
    first = max(f1, target_f)
    last = min(l1, target_l)

    non_intersected_before_first = -1
    non_intersected_before_last = -1

    intersected_first = -1
    intersected_last = -1

    non_intersected_after_first = -1
    non_intersected_after_last = -1

    if first > last:
        # non intersecting
        if first < target_f:
            non_intersected_before_first = f1
            non_intersected_before_last = l1
        else:
            non_intersected_after_first = f1
            non_intersected_after_last = l1
    else:
        # intersecting
        if f1 < first:
            non_intersected_before_first = f1
            non_intersected_before_last = first - 1

        if l1 > last:
            non_intersected_after_first = last + 1
            non_intersected_after_last = l1

        intersected_first = first
        intersected_last = last

    return non_intersected_before_first, non_intersected_before_last, intersected_first, intersected_last, non_intersected_after_first, non_intersected_after_last


def process_block(
        source_values_first: List[int],
        source_values_last: List[int],
        sources_first: List[int],
        sources_last: List[int],
        destinations_first: List[int],
):
    """
    Building block for mapping a source to destination
    :param source_values_first: list of first values of source intervals
    :param source_values_last: list of last values of source intervals
    :param sources_first: list of first values of source intervals of the mapping
    :param sources_last: list of last values of source intervals of the mapping
    :param destinations_first: list of first values of destination intervals of the mapping
    :return: new_dest_first, new_dest_last : A tuple with two lists
    containing the first and last values of the new destination intervals
    """
    new_dest_first = []
    new_dest_last = []

    i = 0
    j = 0
    while i < len(source_values_first):
        non_intersected_before_first, non_intersected_before_last, intersected_first, intersected_last, non_intersected_after_first, non_intersected_after_last = get_intersected_first_last(
            source_values_first[i], source_values_last[i],
            sources_first[j], sources_last[j]
        )

        non_intersected_before = False
        intersected = False
        non_intersected_after = False

        if non_intersected_before_first != -1:
            new_dest_first.append(non_intersected_before_first)
            new_dest_last.append(non_intersected_before_last)
            non_intersected_before = True

        if intersected_first != -1:
            new_dest_first.append(destinations_first[j] + (intersected_first - sources_first[j]))
            new_dest_last.append(destinations_first[j] + (intersected_last - sources_first[j]))
            source_values_first[i] = intersected_last + 1
            intersected = True

        if non_intersected_after_first != -1:
            source_values_first[i] = non_intersected_after_first
            source_values_last[i] = non_intersected_after_last
            non_intersected_after = True

        if non_intersected_after:
            j += 1
            if j == len(sources_first):
                for i in range(i, len(source_values_first)):
                    new_dest_first.append(source_values_first[i])
                    new_dest_last.append(source_values_last[i])
                break

        if intersected and not non_intersected_after:
            i += 1

        if non_intersected_before and not intersected and not non_intersected_after:
            i += 1

    return new_dest_first, new_dest_last


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        first_line = f.readline()
        maps = f.read()

    raw_source_values = list(map(lambda x: int(x), re.findall(r'\s*(\d+)\s*', first_line)))
    source_values_first = raw_source_values[::2]
    source_values_last = []

    for i, source_length in enumerate(raw_source_values[1::2]):
        source_values_last.append(source_values_first[i] + source_length - 1)

    # I assumed non overlapping sets
    source_values_first.sort()
    source_values_last.sort()

    maps = maps.split('\n\n')
    for raw_map in maps:
        map_values = list(map(lambda x: int(x), re.findall(r'\s*(\d+)\s*', raw_map)))

        destinations_first = map_values[::3]
        sources_first = map_values[1::3]
        ranges = map_values[2::3]

        assert len(destinations_first) == len(sources_first) == len(ranges)

        sources_last = []
        destinations_last = []

        for i, sd_length in enumerate(ranges):
            sources_last.append(sources_first[i] + sd_length - 1)

        old_sources_first = sources_first.copy()
        sources_first.sort()
        sorted_sources_first = sources_first
        sorted_sources_last = []
        sorted_destination_first = []

        for sorted in sources_first:
            index = old_sources_first.index(sorted)
            sorted_sources_last.append(sources_last[index])
            sorted_destination_first.append(destinations_first[index])

        source_values_first, source_values_last = process_block(
            source_values_first,
            source_values_last,
            sorted_sources_first,
            sorted_sources_last,
            sorted_destination_first,
        )

        source_values_first.sort()
        source_values_last.sort()

    print(source_values_first[0])
