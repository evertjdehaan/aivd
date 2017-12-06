import numpy as np


def solve_part1(jump_list):
    # Set the current, minimum and maximum positions
    position_cur = 0
    position_max = len(jump_list) - 1
    position_min = 0

    num_steps = 0
    while position_max >= position_cur >= position_min:
        # Add the jump instruction to the current position
        position_next = position_cur + jump_list[position_cur]

        # +1 the value at the current position
        jump_list[position_cur] += 1

        # Increase the number of steps and update the position
        num_steps += 1
        position_cur = position_next

    return num_steps


def solve_part2(jump_list):
    # Set the current, minimum and maximum positions
    position_cur = 0
    position_max = len(jump_list) - 1
    position_min = 0

    num_steps = 0
    while position_max >= position_cur >= position_min:
        # Add the jump instruction to the current position
        position_next = position_cur + jump_list[position_cur]

        # +1 the value at the current position, except if the offset is 3 or
        # more, then decrease it by one
        if jump_list[position_cur] >= 3:
            jump_list[position_cur] -= 1
        else:
            jump_list[position_cur] += 1

        # Increase the number of steps and update the position
        num_steps += 1
        position_cur = position_next

    return num_steps


if __name__ == '__main__':
    # solve problem 1
    assert solve_part1([0, 3, 0, 1, -3]) == 5
    jump_list = np.genfromtxt('day05_input.txt', int)
    print(solve_part1(jump_list))

    # solve problem 2
    assert solve_part2([0, 3, 0, 1, -3]) == 10
    jump_list = np.genfromtxt('day05_input.txt', int)
    print(solve_part2(jump_list))
