import numpy as np
import re


def _remove_garbage(text):
    # Replace all exclamation marks and the following characters
    cleaner_text = re.sub('!.{1}', '', text)

    # Replace all garbage
    (clean_text, num_subs) = re.subn('<.*?>', '', cleaner_text)

    # Determine the number of cleaned characters (excluding the < and >)
    chars_del = len(cleaner_text) - len(clean_text) - num_subs * 2

    return clean_text, chars_del


def solve_part1(text):
    # First remove the garbage
    clean_text, chars_del = _remove_garbage(text)

    level = 0
    score = 0
    for i in range(len(clean_text)):
        if clean_text[i] == '{':
            level += 1
        elif clean_text[i] == '}':
            score += level
            level -= 1

    return score


def solve_part2(text):
    # First remove the garbage
    clean_text, chars_del = _remove_garbage(text)

    return chars_del


if __name__ == '__main__':
    # Get the full problem text
    with open('day09_input.txt', 'r') as f:
        full_text = f.read()

    assert solve_part1('{}') == 1
    assert solve_part1('{{{}}}') == 6
    assert solve_part1('{{},{}}') == 5
    assert solve_part1('{{{},{},{{}}}}') == 16
    assert solve_part1('{<a>,<a>,<a>,<a>}') == 1
    assert solve_part1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert solve_part1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert solve_part1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
    print(solve_part1(full_text))

    assert solve_part2('<>') == 0
    assert solve_part2('<random characters>') == 17
    assert solve_part2('<<<<>') == 3
    assert solve_part2('<{!>}>') == 2
    assert solve_part2('<!!>') == 0
    assert solve_part2('<!!!>>') == 0
    assert solve_part2('<{o"i!a,<{i<a>') == 10
    print(solve_part2(full_text))
