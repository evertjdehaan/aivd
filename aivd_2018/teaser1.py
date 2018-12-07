import numpy as np
from itertools import combinations_with_replacement

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
