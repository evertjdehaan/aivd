import numpy as np


def solve_part1(_range, lengths):
    local_range = _range
    # Initialize the skip size and start position
    skip_size = 0
    start_posistion = 0

    for length in lengths:
        # Select the values in the length
        end_position = start_posistion + length
        if end_position > len(local_range):
            wrap_around = True
            end_position = end_position % len(local_range)
            temp_array = np.concatenate((
                local_range[start_posistion:len(local_range)],
                local_range[0:end_position]
            ))
        else:
            wrap_around = False
            temp_array = local_range[start_posistion:end_position]

        # Reverse the values in the length
        temp_array = temp_array[::-1]

        # Write back the results in the array
        if wrap_around:
            local_range[start_posistion:len(local_range)] = \
                temp_array[0:len(local_range) - start_posistion]
            local_range[0:end_position] = \
                temp_array[len(local_range) - start_posistion:]
        else:
            local_range[start_posistion:end_position] = temp_array

        # Update the start position, making sure it wraps around
        start_posistion = (start_posistion + length + skip_size) % len(local_range)

        # Increase the skip size by one
        skip_size += 1

    return local_range[0] * local_range[1], local_range


if __name__ == '__main__':
    full_range = np.arange(0, 256)
    full_lengths = [94, 84, 0, 79, 2, 27, 81, 1, 123, 93, 218, 23, 103, 255,
                    254, 243]

    test_range = np.arange(0, 5)
    test_lengths = [3, 4, 1, 5]

    assert solve_part1(test_range, test_lengths)[0] == 12
    print(solve_part1(full_range, full_lengths)[0])
