def int_to_roman(integer):
  """ Convert an integer to a Roman numeral.
  Kudos: Python Cookbook by David Ascher, Alex Martelli
  """
  ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
  nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
  result = []
  for i in range(len(ints)):
    count = int(integer / ints[i])
    result.append(nums[i] * count)
    integer -= ints[i] * count
  return ''.join(result)

def is_odd(num):
  if num % 2 == 1:
    return True
  return False

def is_prime(num):
  is_prime = True
  for i in range(2, int(num/2)):
    if num % i == 0:
      is_prime = False
      break
  return is_prime

def divisors_from_list(num, divisor_list):
  div_list = []
  for div in divisor_list:
    if num % div == 0 and num != div:
      div_list.append(div)
  return div_list

def in_list(num, lst):
  if num in lst:
    return True
  return False

# Search all numbers from 0 to 3999
number_range = list(range(3999))
# Select only the roman numbers with a length of five letters
valid_roman = {num: int_to_roman(num) for num in number_range if len(int_to_roman(num)) == 5}
print('All')
print(list(valid_roman.keys()))
print(list(valid_roman.values()))

# F is only odd numbers
print('Odd')
print(list(map(is_odd, valid_roman.keys())))

# C is a prime
print('Prime')
print(list(map(is_prime, valid_roman.keys())))

# E has J as divisor
has_divisors = [divisors_from_list(num, valid_roman.keys()) for num in valid_roman.keys()]
print('Divisors per number')
for div in has_divisors:
  print(div)

# J is a divisor of E
unique_divs = []
for div in has_divisors:
  for d in div:
    unique_divs.append(d)
unique_divs = list(set(unique_divs))
is_divisor = [in_list(num, unique_divs) for num in valid_roman.keys()]
print('Unique divisors')
print(is_divisor)
