import re


def solve_part1(towers):
    # Create a list for the (sub)tower bottoms
    tower_bottoms = []
    # Create a list for the (sub)tower tops
    tower_tops = []

    for tower in towers:
        # Find the bottom and tops (if any)
        match = re.match('(?P<bottom>.+?) \(\d+\) -> (?P<top>.+)', tower)

        if match is None:
            match = re.match('(?P<bottom>.+?) \(\d+\)', tower)
            tower_bottoms.append(match.group('bottom'))
        else:
            tower_bottoms.append(match.group('bottom'))
            tower_tops.extend(
                match.group('top').split(', ')
            )

    overall_bottom = set(tower_bottoms) - set(tower_tops)

    return overall_bottom.pop()


if __name__ == '__main__':
    # Get the tower set
    with open('day07_input.txt', 'r') as f:
        full_text = f.readlines()
    with open('day07_test.txt', 'r') as f:
        test_text = f.readlines()

    assert solve_part1(test_text) == 'tknk'
    print(solve_part1(full_text))
