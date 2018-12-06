def solve_part1(file_path):
  doubles = 0
  triples = 0

  with open(file_path, 'r') as f:
    for full_id in f:
      # Get a list of unique characters in the string
      unique_chars = list(set(full_id))
      # Check if the unique letters occur exactly two or threee times
      frequencies = []
      for char in unique_chars:
        frequencies.append(full_id.count(char))

      # Check if one or more letters appear once or twice
      if 2 in frequencies:
        doubles += 1
      if 3 in frequencies:
        triples += 1

  return doubles * triples

def _find_common_chars_matching_IDs(id_list):
  common_chars = False

  # Check if any of the two adjacent ones differ by one character
  for i in range(len(id_list)-1):
    # Count the number of different characters
    chars_same = [id_list[i][j]==id_list[i+1][j] for j in range(len(id_list[i]))]
    num_diff_chars = len(id_list[i]) - sum(chars_same)

    if num_diff_chars == 1:
      # Get all characters of the ID
      chars = list(id_list[i])
      # Remove the different character
      chars[chars_same.index(False)] = ''
      common_chars = ''.join(chars)

      print(id_list[i])
      print(id_list[i+1])

      break

  return common_chars

def solve_part2(file_path):
  # Brute forcing (comparing each ID with all other IDs) is slow (O(N^2)). There is a faster idea (O(2N)).
  common_chars = ''

  # Read all IDs and sort them alphabetically
  id_list = []
  with open(file_path, 'r') as f:
    id_list = f.read().splitlines()
  id_list.sort()

  # Check if any of the two adjacent ones differ by one character and get the common characters
  common_chars = _find_common_chars_matching_IDs(id_list)

  # If there was no match, the first character was the different one, so we reverse the sort and do the same trick again
  if common_chars == False:  
    # Reverse all the ID strings
    id_list = [x[::-1] for x in id_list]
    # Sort the IDs alphabetically
    id_list.sort()
    # Check if any of the two adjacent ones differ by one character and get the common characters
    common_chars = _find_common_chars_matching_IDs(id_list)

  return common_chars


if __name__ == '__main__':
    # solve problem 1
    assert solve_part1('day02_test1.txt') == 12
    print(solve_part1('day02_input.txt'))

    # solve problem 2
    assert solve_part2('day02_test2.txt') == 'fgij'
    print(solve_part2('day02_input.txt'))
