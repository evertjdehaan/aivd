import re
import unicodedata

WORDSPATH = r'C:\Users\EVEHAA\Documents\GitHub\puzzles\OpenTaal-210G-basis-gekeurd.txt'


def _get_word_pattern(word):
    letter_count = 0

    pattern = word
    for char in pattern:
        if char.islower():
            pattern = pattern.replace(char, chr(ord('A')+letter_count))
            letter_count += 1

    return pattern


def _get_unicode(word):
    return ''.join(
        (c for c in unicodedata.normalize('NFD', word)
         if unicodedata.category(c) != 'Mn')
    )


def getwords(length=None, length_minimum=None, length_maximum=None, regex=None,
             pattern=None):
    # Define the allowed characters
    allowed_chars = [chr(o) for o in range(ord("a"), ord("z")+1)]

    if length is not None:
        length_minimum = length
        length_maximum = length

    # Turn the pattern into a standardized pattern for easy comparison and
    # set the minimum and the maximum length the the length of the pattern
    if pattern is not None:
        length_minimum = len(pattern)
        length_maximum = len(pattern)
        pattern = _get_word_pattern(pattern)

    words = set()
    with open(WORDSPATH) as f:
        for line in f:
            word = _get_unicode(line.strip().lower())

            # Check if the maximum length is not exceeded
            if length_maximum is not None and len(word) > length_maximum:
                continue
            # Check if the minimum length is not exceeded
            if length_minimum is not None and len(word) < length_minimum:
                continue
            # Check if the regex is matched
            if regex is not None and not re.match(regex, word):
                continue
            # Check if the pattern is matched
            if pattern is not None and (pattern != _get_word_pattern(word)):
                continue

            # If all characters are allowed, add the word to the list
            if (set(allowed_chars) | set(word)) == set(allowed_chars):
                words.add(word)

    return words


if __name__ == '__main__':
    print(getwords(pattern='sxeolfdwlh'))
