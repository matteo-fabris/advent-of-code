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

        # init maximum values for each color
        # in the game
        max_red = 0
        max_green = 0
        max_blue = 0

        for subset in subsets:
            # Find all red, green, and blue blocks
            red_blocks = re.findall(r'\s*(\d+)\s*red', subset)
            green_blocks = re.findall(r'\s*(\d+)\s*green', subset)
            blue_blocks = re.findall(r'\s*(\d+)\s*blue', subset)

            # Sum the blocks for each color
            # and update the maximum values
            # if exceeded the current maximum
            if sum(list(map(int, red_blocks))) > max_red:
                max_red = sum(list(map(int, red_blocks)))

            if sum(list(map(int, green_blocks))) > max_green:
                max_green = sum(list(map(int, green_blocks)))

            if sum(list(map(int, blue_blocks))) > max_blue:
                max_blue = sum(list(map(int, blue_blocks)))

        # Add the product of the maximum values
        result += (max_red*max_green*max_blue)

    print(result)
