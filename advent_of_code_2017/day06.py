import numpy as np


def solve(bank_list):
    # Make a placeholder for
    past_states = []

    # Get the number of memory banks
    num_banks = len(bank_list)

    num_steps = 0
    while True:
        # If the current step already occurred before, stop
        if list(bank_list) in past_states:
            break

        # Add the new state to the list of past_states
        past_states.append(list(bank_list))

        # Determine the location from which to take the blocks
        # (argmax automatically takes the first encounter)
        position = bank_list.argmax()
        cur_blocks = bank_list[position]

        # Determine how many blocks all of the banks get and how many units
        # remain to be distributed over the first few
        blocks_all = cur_blocks // num_banks
        blocks_rem = cur_blocks % num_banks

        # Remove the blocks from the current place
        bank_list[position] = 0

        # Distribute the blocks
        bank_list += np.array([blocks_all]*num_banks)
        bank_list[position+1:min(position+blocks_rem+1, num_banks)] += 1
        bank_list[0:max(blocks_rem-(num_banks-position)+1, 0)] += 1

        # Go to the next step
        num_steps += 1

    # Determine the length of the infinite loop (part 2)
    loop_length = len(past_states) - past_states.index(list(bank_list))

    return [num_steps, loop_length]


if __name__ == '__main__':
    # solve both problems
    assert solve(np.array([0, 2, 7, 0])) == [5, 4]
    print(solve(
        np.array([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])
    ))
