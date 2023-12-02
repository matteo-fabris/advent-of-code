import re


def multiple_replace_recursive(text: str, replacements: dict) -> str:
    """
    Helper function to replace multiple strings in a text.

    :param text:
    :param replacements:
    :return:
    """
    regex = re.compile("(%s)" % "|".join(replacements.keys()))
    processed_text = regex.sub(lambda m: replacements[m.group()], text)
    if processed_text == text:
        # if nothing was replaced, we are done
        return processed_text
    else:
        # if something was replaced, we need to check again
        # since more replacements might be possible
        return multiple_replace_recursive(processed_text, replacements)


# Define a custom replacement_dict
# note that some letters are preserved
# to allow overlapping strings
#  e.g. oneight -> o1eight -> o1e8t
replacement_dict = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': '4',
    'five': '5e',
    'six': '6',
    'seven': '7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

if __name__ == '__main__':

    result = 0
    with open('input.txt', 'r') as f:
        # We need to replace the strings multiple times
        # because of overlapping strings.
        # E.g. oneight -> o1eight -> o1e8t
        replaced_file_content = multiple_replace_recursive(f.read(), replacement_dict)

        # Remove all letters
        digits_only = re.sub(r'[a-zA-Z]*', '', replaced_file_content)

        # For every line we keep first
        # and last digit and add them to the sum
        for digits in digits_only.split('\n'):
            if len(digits) > 0:
                result += int(digits[0] + digits[-1])

    print(result)
