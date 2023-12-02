import re

if __name__ == '__main__':

    result = 0
    with open('input.txt', 'r') as f:
        games = f.readlines()

    for game in games:
        # Retrieve the game id
        m = re.search(r'(?<=Game )\d+', game)
        game_id = m.group(0)

        # Retrieve all subgames
        subsets = re.split(r': |; ', game)[1:]
        is_valid = True

        for subset in subsets:
            if not is_valid:
                break

            # Find all red, green, and blue blocks
            red_blocks = re.findall(r'\s*(\d+)\s*red', subset)
            green_blocks = re.findall(r'\s*(\d+)\s*green', subset)
            blue_blocks = re.findall(r'\s*(\d+)\s*blue', subset)

            # Check if the number of blocks exceeds the limit
            if sum(list(map(int, red_blocks))) > 12 or sum(list(map(int, green_blocks))) > 13 or sum(list(map(int, blue_blocks))) > 14:
                is_valid = False

        # if all subsets are valid, add the game id to the result
        if is_valid:
            result += int(game_id)

    print(result)
