def _passphrase_valid1(passphrase):
    # Split the passphrase in a list of words
    list_words = passphrase.split()

    # Determine if there are non-unique items in the passphrase
    return len(set(list_words)) == len(list_words)



def _passphrase_valid2(passphrase):
    # Split the passphrase in a list of words
    list_words = passphrase.split()

    # Determine if there are non-unique items in the passphrase
    if len(set(list_words)) != len(list_words):
        return False

    # Sort the letters of each word to expose the anagrams
    sorted_words = [''.join(sorted(word)) for word in list_words]

    # Determine if there are non-unique items in the sorted passphrase words
    return len(set(sorted_words)) == len(sorted_words)


def solve_part1(file_path):
    num_valid = 0

    with open(file_path, 'r') as f:
        # Loop over the passphrases
        for passphrase in f:
            if _passphrase_valid1(passphrase):
                num_valid += 1

    return num_valid


def solve_part2(file_path):
    num_valid = 0

    with open(file_path, 'r') as f:
        # Loop over the passphrases
        for passphrase in f:
            if _passphrase_valid2(passphrase):
                num_valid += 1

    return num_valid

if __name__ == '__main__':
    # solve problem 1
    assert _passphrase_valid1('aa bb cc dd ee') == True
    assert _passphrase_valid1('aa bb cc dd aa') == False
    assert _passphrase_valid1('aa bb cc dd aaa') == True
    print(solve_part1('day04_test.txt'))

    # solve problem 2
    assert _passphrase_valid2('abcde fghij') == True
    assert _passphrase_valid2('abcde xyz ecdab') == False
    assert _passphrase_valid2('a ab abc abd abf abj') == True
    assert _passphrase_valid2('iiii oiii ooii oooi oooo') == True
    assert _passphrase_valid2('oiii ioii iioi iiio') == False
    print(solve_part2('day04_test.txt'))
