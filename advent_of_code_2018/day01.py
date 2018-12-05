def solve_part1(file_path):
  freq = 0

  with open(file_path, 'r') as f:
    # Add all the changes in the file to get the final frequency
    for change in f:
      freq += int(change)

  return freq

def solve_part2(file_path):
  # Create an array to contain the found frequencies
  past_freqs = [0]
  cur_freq = 0
  stop = False

  # Update the frequency until a past frequency is found, reopen the file if necessary
  while not stop:
    with open(file_path, 'r') as f:
      for change in f:
        # Calculate the new frequency
        cur_freq += int(change)
        
        # Add the frequency, if not already in the list
        if cur_freq in past_freqs:
          stop = True
          break
        past_freqs.append(cur_freq)

  return cur_freq


if __name__ == '__main__':
    # solve problem 1
    assert solve_part1('day01_test1.txt') == 3
    print(solve_part1('day01_input.txt'))

    # solve problem 2
    assert solve_part2('day01_test1.txt') == 2
    assert solve_part2('day01_test2.txt') == 10
    print(solve_part2('day01_input.txt'))
