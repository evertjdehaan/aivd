from copy import deepcopy

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


######## Part 2 #############
print('\n\n\n')
def update_options(lst, ch0, ch1, ch2, ch3, ch4=['M', 'D', 'C', 'L', 'X', 'V', 'I']):
  return [num for num in lst
        if int_to_roman(num)[0] in ch0 and
          int_to_roman(num)[1] in ch1 and
          int_to_roman(num)[2] in ch2 and
          int_to_roman(num)[3] in ch3 and
          int_to_roman(num)[4] in ch4]

def update_all_lists(b, c, d, e, f, g, h, i, j):
  d0 = list(set([int_to_roman(num)[1] for num in f]))
  d1 = list(set([int_to_roman(num)[1] for num in g]))
  d2 = list(set([int_to_roman(num)[1] for num in h]))
  d3 = list(set([int_to_roman(num)[1] for num in i]))
  d4 = list(set([int_to_roman(num)[1] for num in j]))
  d = update_options(d, d0, d1, d2, d3, d4)
  f = d

  f0 = list(set([int_to_roman(num)[0] for num in e]))
  f1 = list(set([int_to_roman(num)[0] for num in d]))
  f2 = list(set([int_to_roman(num)[0] for num in c]))
  f3 = list(set([int_to_roman(num)[0] for num in b]))
  f = update_options(f, f0, f1, f2, f3)
  d = f
  
  b0 = list(set([int_to_roman(num)[3] for num in f]))
  b1 = list(set([int_to_roman(num)[3] for num in g]))
  b2 = list(set([int_to_roman(num)[3] for num in h]))
  b3 = list(set([int_to_roman(num)[3] for num in i]))
  b4 = list(set([int_to_roman(num)[3] for num in j]))
  b = update_options(b, b0, b1, b2, b3, b4)

  c0 = list(set([int_to_roman(num)[2] for num in f]))
  c1 = list(set([int_to_roman(num)[2] for num in g]))
  c2 = list(set([int_to_roman(num)[2] for num in h]))
  c3 = list(set([int_to_roman(num)[2] for num in i]))
  c4 = list(set([int_to_roman(num)[2] for num in j]))
  c = update_options(c, c0, c1, c2, c3, c4)

  e0 = list(set([int_to_roman(num)[0] for num in f]))
  e1 = list(set([int_to_roman(num)[0] for num in g]))
  e2 = list(set([int_to_roman(num)[0] for num in h]))
  e3 = list(set([int_to_roman(num)[0] for num in i]))
  e4 = list(set([int_to_roman(num)[0] for num in j]))
  e = update_options(e, e0, e1, e2, e3, e4)

  g0 = list(set([int_to_roman(num)[1] for num in e]))
  g1 = list(set([int_to_roman(num)[1] for num in d]))
  g2 = list(set([int_to_roman(num)[1] for num in c]))
  g3 = list(set([int_to_roman(num)[1] for num in b]))
  g = update_options(g, g0, g1, g2, g3)

  h0 = list(set([int_to_roman(num)[2] for num in e]))
  h1 = list(set([int_to_roman(num)[2] for num in d]))
  h2 = list(set([int_to_roman(num)[2] for num in c]))
  h3 = list(set([int_to_roman(num)[2] for num in b]))
  h = update_options(h, h0, h1, h2, h3)

  i0 = list(set([int_to_roman(num)[3] for num in e]))
  i1 = list(set([int_to_roman(num)[3] for num in d]))
  i2 = list(set([int_to_roman(num)[3] for num in c]))
  i3 = list(set([int_to_roman(num)[3] for num in b]))
  i = update_options(i, i0, i1, i2, i3)

  j0 = list(set([int_to_roman(num)[4] for num in e]))
  j1 = list(set([int_to_roman(num)[4] for num in d]))
  j2 = list(set([int_to_roman(num)[4] for num in c]))
  j3 = list(set([int_to_roman(num)[4] for num in b]))
  j = update_options(j, j0, j1, j2, j3)

  # Filter e for those divisors that are still available
  has_divisors = [divisors_from_list(num, j) for num in e]
  e = [e[i] for i in range(len(e)) if len(has_divisors[i]) > 0]

  return b, c, d, e, f, g, h, i, j

def print_lists(b, c, d, e, f, g, h, i, j):
  print('B ({})\n'.format(len(b)), b)
  print('C ({})\n'.format(len(c)), c)
  print('D ({})\n'.format(len(d)), d)
  print('E ({})\n'.format(len(e)), e)
  print('F ({})\n'.format(len(f)), f)
  print('G ({})\n'.format(len(g)), g)
  print('H ({})\n'.format(len(h)), h)
  print('I ({})\n'.format(len(i)), i)
  print('J ({})\n'.format(len(j)), j)

def print_options_a(f, g, h, i, j):
  a0 = list(set([int_to_roman(num)[4] for num in f]))
  a1 = list(set([int_to_roman(num)[4] for num in g]))
  a2 = list(set([int_to_roman(num)[4] for num in h]))
  a3 = list(set([int_to_roman(num)[4] for num in i]))
  a4 = list(set([int_to_roman(num)[4] for num in j]))
  print('Options A\n', a0, a1, a2, a3, a4)

# Start with complete sets of options
B = valid_roman.keys()
C = valid_roman.keys()
D = valid_roman.keys()
E = valid_roman.keys()
F = valid_roman.keys()
G = valid_roman.keys()
H = valid_roman.keys()
I = valid_roman.keys()
J = valid_roman.keys()

### Step 1
# Select only odd numbers
F = [num for num in F if is_odd(num)]
# Remove numbers with "I"s (the letters of D are the second letters of the five-letter vertical numbers, which cannot be "I"s)
F = [num for num in F if not "I" in valid_roman[num]]
D = F
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 2
# The first two numbers of D and F should be the same
F = [num for num in F if valid_roman[num][0] == valid_roman[num][1]]
D = F
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 3
# C should be a prime
C = [num for num in C if is_prime(num)]
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 4
# E should have divisors in the list
E = [num for num in E if len(has_divisors[list(valid_roman.keys()).index(num)]) > 0]
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 5
# J should have multiples in the list
J = [num for num in J if is_divisor[list(valid_roman.keys()).index(num)]]
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 6
# Done inherently

### Step 7
# Done inherently

### Step 8
# Done inherently

### Step 9
# C - D + I = C + I + I (or: C - D + I = 102)
options_c = []
options_d = []
options_i = []
for c in C:
  for d in D:
    for i in I:
      if c - d + i == 102:
        options_c.append(c)
        options_d.append(d)
        options_i.append(i)
C = sorted(list(set(options_c)))
D = sorted(list(set(options_d)))
I = sorted(list(set(options_i)))
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

### Step 10
# B + E = G + H
options_b = []
options_e = []
options_g = []
options_h = []
for b in B:
  for e in E:
    for g in G:
      for h in H:
        if b + e == g + h:
          options_b.append(b)
          options_e.append(e)
          options_g.append(g)
          options_h.append(h)
B = sorted(list(set(options_b)))
E = sorted(list(set(options_e)))
G = sorted(list(set(options_g)))
H = sorted(list(set(options_h)))
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

print_lists(B, C, D, E, F, G, H, I, J)
print_options_a(F, G, H, I, J)

### Brute force all remaining options
works_C = []
works_D = []
works_E = []
for c in C:
  for d in D:
    for e in E:
      try_B, try_C, try_D, try_E, try_F, try_G, try_H, try_I, try_J = update_all_lists(B, [c], [d], [e], F, G, H, I, J)
      if len(try_B) > 0 and len(try_G) > 0 and len(try_H) > 0 and len(try_I) > 0 and len(try_J) > 0:
        # C, D and E are preset, F equals D
        works_C.append(c)
        works_D.append(d)
        works_E.append(e)

try_B, try_C, try_D, try_E, try_F, try_G, try_H, try_I, try_J = update_all_lists(B, list(set(works_C)), list(set(works_D)), list(set(works_E)), F, G, H, I, J)
print_lists(try_B, try_C, try_D, try_E, try_F, try_G, try_H, try_I, try_J)
print_options_a(try_F, try_G, try_H, try_I, try_J)

### Solution AVICII
F = [num for num in F if valid_roman[num][4] == 'V']
G = [num for num in G if valid_roman[num][4] == 'I']
H = [num for num in H if valid_roman[num][4] == 'C']
I = [num for num in I if valid_roman[num][4] == 'I']
J = [num for num in J if valid_roman[num][4] == 'I']
# Update the intersecting numbers
B, C, D, E, F, G, H, I, J = update_all_lists(B, C, D, E, F, G, H, I, J)

print()
print('--- AVICII ---')
print_lists(B, C, D, E, F, G, H, I, J)
print_options_a(F, G, H, I, J)
