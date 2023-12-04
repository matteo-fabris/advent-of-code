import re

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        cards = f.readlines()

    total_cards_per_number = [1]*len(cards)

    for i, card in enumerate(cards):
        # Retrieve all subsets
        subsets = re.split(r': | \| ', card)[1:]

        winning_numbers = re.findall(r'\s*(\d+)\s*', subsets[0])
        numbers_you_have = re.findall(r'\s*(\d+)\s*', subsets[1])

        n_matches = len(set(winning_numbers).intersection(set(numbers_you_have)))

        if n_matches > 0:

            for j in range(
                    min(len(cards)-1, i+1),
                    min(len(cards), i+n_matches+1)
            ):
                total_cards_per_number[j] += 1 * total_cards_per_number[i]

    print(sum(total_cards_per_number))
