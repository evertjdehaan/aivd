import numpy as np


def solve_part1(core_matrix):
    # Get all the maximum and minimum values of the rows
    max_row = np.nanmax(core_matrix, axis=1)
    min_row = np.nanmin(core_matrix, axis=1)

    # Determine the sum of difference of the max and the min (the checksum
    return sum(max_row - min_row)


def solve_part2(core_matrix):
    total = 0

    for row in range(core_matrix.shape[0]):
        # Get the relevant row
        row_array = core_matrix[row, :]

        # Repeat the row as columns, so [1, 2, 3] becomes
        # [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        rep_mat = np.tile(row_array, (len(row_array), 1)).T

        # Divide the just-formed matrix by the elements of the row
        div_mat_float = rep_mat / row_array

        # Convert the division matrix to an integer
        div_mat_int = div_mat_float.astype(int)

        # Find the location in the first matrix which were integer
        int_locations = (div_mat_float == div_mat_int)

        # Remove the diagonal elements (they always evenly divide)
        int_locations = int_locations - np.eye(len(row_array))

        # Get the sought-after number
        total += int(div_mat_int[np.nonzero(int_locations)])

    return total


if __name__ == '__main__':
    # The puzzle input
    full_code = np.genfromtxt('day02_input.txt', int)

    # solve problem 1
    # test_code1 = np.genfromtxt('day02_test1.txt', int,
    #                           usecols=range(0, 4))
    # assert solve_part1(test_code1) == 18
    print(solve_part1(full_code))

    # solve problem 2
    test_code = np.genfromtxt('day02_test2.txt', int)
    assert solve_part2(test_code) == 9
    print(solve_part2(full_code))
