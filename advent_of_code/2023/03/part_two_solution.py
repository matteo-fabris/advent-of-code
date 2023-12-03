import re


def get_positions_to_check(row_len : int, start_index: int, end_index: int):
    # lateral positions
    positions = [end_index, start_index - 1]
    # vertical positions (including diagonals)
    for i in range(start_index - 1, end_index + 1):
        positions.append(i + row_len)
        positions.append(i - row_len)
    return positions


if __name__ == '__main__':

    result = 0
    with open('input.txt', 'r') as f:
        file_content = f.read()

    row_len = len(re.match(r'.*\n', file_content).group(0))

    # add vertical padding
    file_content = '.' * row_len + file_content + '.' * row_len

    star_indexes = [m.start() for m in re.finditer('\*', file_content)]
    candidate_gears = {key: [] for key in star_indexes}

    # for each number
    for m in re.finditer(r'\d+', file_content):
        start_index = m.start()
        end_index = m.end()
        number = int(str(file_content[start_index:end_index]))

        positions_to_check = get_positions_to_check(row_len, start_index, end_index)

        intersecting_stars = set(positions_to_check).intersection(set(star_indexes))
        # for each star in the neighborhood of the number
        for intersecting_star in intersecting_stars:
            candidate_gears[intersecting_star].append(number)

    # At this point, candidate_gears contains
    # {star_index: [number_1, number_2, ...], ...}
    # we just need to keep only lists
    # with 2 elements

    for candidate_gear in candidate_gears.values():
        if len(candidate_gear) == 2:
            result += candidate_gear[0]*candidate_gear[1]

    print(result)
