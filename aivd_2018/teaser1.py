import numpy as np
from itertools import combinations_with_replacement, permutations
from .getwords import getwords

def find_letters():
  target_sums = [22, 67, 59, 56, 77, 72, 30, 67]
  target_products = [216 , 67200, 24840, 21450, 122892, 95760, 3150, 61560]
  line = 0

  for (target_sum, target_product) in zip(target_sums, target_products):
    line += 1

    # Get the divisors of the product in the range of 1-26
    divisors = []
    for divisor in range(1, 27):
      if target_product % divisor == 0:
        divisors.append(divisor)

    # Get all combinations of length five (the puzzle size)
    options = combinations_with_replacement(divisors, 5)

    # Find the options of which the sum matches the target sum and the product matches the target product
    for option in options:
      option = np.array(option)
      if option.sum() == target_sum and option.prod() == target_product:
        print(line, option, ''.join([chr(64+x) for x in option]))

def find_words_bottom():
  part1 = set(permutations('AOPSU', 2))
  part2 = set(permutations('CCEEN', 3))
  part3 = set(permutations('AIRST', 5))
  part4 = set(permutations('CCEEN', 2))

  strings = []
  for p1 in part1:
    for p2 in part2:
      for p3 in part3:
        for p4 in part4:
          # Only add the string if part2 + part4 = CCEEN
          if ''.join(sorted(''.join(p2)+''.join(p4))) == 'CCEEN':
            strings.append(''.join(p1)+''.join(p2)+''.join(p3)+''.join(p4))

  # Get words with a length of 4-10, containing only allowed letters and at least containing one c
  words = getwords(length_minimum=4, length_maximum=10, regex='^[aceinoprstu]*c[aceinoprstu]*$')

  # Feedback on the dimension of the problem to be solved
  print(len(strings), len(words))

  # For each word, store the matched strings in a file
  with open('result.txt', 'a') as f:
    for word in words:
      for string in strings:
        if word in string.lower():
          # Mark the word in the string
          matched_string = string.lower().replace(word, word.upper())
          # Write the word and the string to a file
          f.write(word + ', ' + matched_string + '\n')
          # Remove the string from the list to be validated (decreases the search size)
          strings.remove(string)
