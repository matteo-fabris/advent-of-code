import re

if __name__ == '__main__':

    result = 0
    with open('input.txt', 'r') as f:
        # Remove all letters
        digits_only = re.sub(r'[a-zA-Z]*', '', f.read())

        # For every line we keep first
        # and last digit and add them to the sum
        for digits in digits_only.split('\n'):
            if len(digits) > 0:
                sum += int(digits[0]+digits[-1])

    print(result)
