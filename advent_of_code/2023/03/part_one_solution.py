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

    # for each number
    for m in re.finditer(r'\d+', file_content):
        start_index = m.start()
        end_index = m.end()
        number = int(file_content[start_index:end_index])

        # get positions to check
        positions_to_check = get_positions_to_check(row_len, start_index, end_index)

        for position in positions_to_check:
            if not file_content[position].isdigit() and file_content[position] != '.' and file_content[position] != '\n':
                result += number
                break

    print(result)
