import numpy as np
from itertools import combinations_with_replacement
from operator import mul

target_sum = 22
target_product = 216 

# Get the divisors of the product in the range of 1-26
divisors = []
for divisor in range(1, 27):
  if target_product % divisor == 0:
    divisors.append(divisor)

# Get all combinations of length five (the puzzle size)
options = combinations_with_replacement(divisors, 5)

# Find the options of which the sum matches the target sum
viable_options = []
for option in options:
  option = np.array(option)
  if option.sum() == target_sum and option.prod() == target_product:
    viable_options.append(option)

for option in viable_options:
  print(option, [chr(64+x) for x in option])
