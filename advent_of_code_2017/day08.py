import re


def solve(instructions):
    registers = {}
    max_value = 0

    for instruction in instructions:
        # Find the relevant parts of the string
        matches = re.match('(?P<target>.+?) (?P<action>.+?) (?P<delta>[-0-9]+) '
                           'if (?P<condition_a>.+?) (?P<condition_b>.+)',
                           instruction)

        # Add the target and conditional registers if they don't already exist
        if not matches.group("target") in registers:
            registers[matches.group("target")] = 0
        if not matches.group("condition_a") in registers:
            registers[matches.group("condition_a")] = 0

        # Determine if the condition is true
        condition_true = eval(
            f'{registers[matches.group("condition_a")]}'
            f'{matches.group("condition_b")}'
        )

        if condition_true:
            # Change the register value
            if matches.group('action') == 'inc':
                registers[matches.group('target')] += int(matches.group('delta'))
            elif matches.group('action') == 'dec':
                registers[matches.group('target')] -= int(matches.group('delta'))

            # Update the maximum value
            max_value = max(max_value, registers[matches.group('target')])

    return max(registers.values()), max_value


if __name__ == '__main__':
    # Get the instruction set
    with open('day08_input.txt', 'r') as f:
        full_text = f.readlines()
    with open('day08_test.txt', 'r') as f:
        test_text = f.readlines()

    assert solve(test_text) == (1, 10)
    print(solve(full_text))
