import itertools

# The letters that need to be replaced
letters = list('EIKLMNRST')

# Get all possible permutations for the numbers 0-9 for these letters
list_perms = itertools.permutations(range(10), len(letters))

# The sum to be solved, moved 'KERST' to the right to check for a zero result
# Start with a space so we can remove leading zeros from numbers later on
eval_sum = ' REKENEN + MET * TIEN - LETTERS - KERST'

# Try all permutations
for perm in list_perms:
  local_eval_sum = eval_sum

  # Replace the letters with the numbers in order of the permutation
  for i in range(len(letters)):
    local_eval_sum = local_eval_sum.replace(letters[i], str(perm[i]))

  # Remove leading zeros from numbers
  local_eval_sum = local_eval_sum.replace(' 0', ' ')

  # Print the magic numbers
  if eval(local_eval_sum) == 0:
      print(dict(zip(letters, perm)))
