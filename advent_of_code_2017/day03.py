# Approach
# There are some important observations regarding the rings
#
# Ring #    Max number on ring  Steps on the diagonal   Steps on the plus
# 0         1                   0                       0
# 1         9                   2                       1
# 2         25                  4                       2
# 3         49                  6                       3
# 4         81                  8                       4
# ...
# n         (2n+1)^2            2n                      n
#
# The numbers on the corners follow a clear pattern as well
#
# Ring #    Corner 1    Corner 2    Corner 3    Corner 4
# 0
# 1         3           5           7           9
# 2         13          17          21          25
# 3         31          37          43          49
# 4         57          65          73          81
# ...
# n         (2n+1)^2-6n (2n+1)^2-4n (2n+1)^2-2n (2n+1)^2

import numpy as np


def _get_ring_corners(ring):
    # Get the corners of the given ring
    return [(2 * ring + 1) ** 2 - 6 * ring,
            (2 * ring + 1) ** 2 - 4 * ring,
            (2 * ring + 1) ** 2 - 2 * ring,
            (2 * ring + 1) ** 2]


def solve_part1(start):
    # Find the ring including the starting location
    ring = 0
    while (2 * ring + 1) ** 2 < start:
        ring += 1

    # Get the corner points of the ring
    corners = _get_ring_corners(ring)

    # Get the distance to the nearest corner
    distance_corner = np.min(np.abs(
        np.array(corners) - np.array([start]*4)
    ))

    # The distance to the center is the distance from the corner (2n),
    # minus the distance to the corner itself
    return 2 * ring - distance_corner


if __name__ == '__main__':
    # solve problem 1
    assert solve_part1(1) == 0
    assert solve_part1(12) == 3
    assert solve_part1(23) == 2
    assert solve_part1(1024) == 31
    print(solve_part1(265149))
