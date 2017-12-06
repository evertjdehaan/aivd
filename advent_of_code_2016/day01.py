import numpy as np


def _get_heading(cur_heading, move):
    # Define the headings and their direction in an x-y plane
    multipliers = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
    headings = list(multipliers.keys())

    # Determine the direction we are turning in
    direction = move[0]

    # Determine the next location
    cur_heading_index = headings.index(cur_heading)
    if direction == 'R':
        if cur_heading_index < len(headings)-1:
            next_heading = headings[cur_heading_index + 1]
        else:
            next_heading = headings[0]
    else:
        if cur_heading_index > 0:
            next_heading = headings[cur_heading_index - 1]
        else:
            next_heading = headings[-1]

    return [next_heading, np.array(multipliers[next_heading])]


def solve_part1(moves_list):
    position = np.array([0, 0])
    heading = 'N'

    for move in moves_list:
        # Get the heading and the direction in the x-y plane
        [heading, multipliers] = _get_heading(heading, move)

        # Determine the change in position
        distance = int(move[1:])
        position += multipliers * np.array([distance]*len(multipliers))

    return sum(np.abs(position))


if __name__ == '__main__':
    # The puzzle input
    with open('day01_input.txt', 'r') as f:
        moves_string = f.read()
    moves_list = moves_string.split(', ')

    # solve problem 1
    assert solve_part1(['R2', 'L3']) == 5
    assert solve_part1(['R2', 'R2', 'R2']) == 2
    assert solve_part1(['R5', 'L5', 'R5', 'R3']) == 12
    print(solve_part1(moves_list))
