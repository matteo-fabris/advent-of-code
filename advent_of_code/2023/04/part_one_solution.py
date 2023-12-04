import re

if __name__ == '__main__':

    result = 0
    with open('input.txt', 'r') as f:
        cards = f.readlines()

    for card in cards:
        # Retrieve all subsets
        subsets = re.split(r': | \| ', card)[1:]

        winning_numbers = re.findall(r'\s*(\d+)\s*', subsets[0])
        numbers_you_have = re.findall(r'\s*(\d+)\s*', subsets[1])

        n_matches = len(set(winning_numbers).intersection(set(numbers_you_have)))

        if n_matches > 0:
            result += 2**(n_matches - 1)

    print(result)
