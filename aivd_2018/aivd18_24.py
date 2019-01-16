from itertools import groupby
from math import ceil

string = [
  'B', 'e', 'e', 'h', 'b', 'k', 'e', 'a', ' ', 'e', 't', 'e', 'd', ' ', ' ', 'l', 'e', 'b', 'a', 'r', 'e', ' ', ' ', 'n', ' ', ' ', 'E',
  'd', 'g', 'p', 'd', 'v', ' ', 'l', 'n', 'i', 'a', ' ', 'e', 'o', 'n', 't', 'k', 'v', 'r', 'l', 's', 'd', ' ', 'e', 't', 'Z', 'a', 'u',
  'E', 'e', 'a', 'e', 'Z', 'l', 'm', 'o', 'a', 'e', 'i', 'h', '.', ' ', 'd', ' ', 't', 'j', 'e', 'n', 't', 'v', 'l', 's', 't', 'o', 'd',
  'd', 's', 'e', 'i', 'o', 'h', 'e', 'r', 'l', 'r', 'e', 'r', 't', 'n', ' ', ' ', 'd', 'e', 'n', 'a', ' ', 'k', 'a', 'n', 'n', 'a', 'r',
  'n', 'n', 'l', ' ', 'd', ' ', 'a', 'v', 'd', 'a', 'i', 'e', 'r', 'a', ' ', 'o', ' ', 'n', ' ', ' ', 'l', 't', 'e', 'e', 'n', ' ', 'r',
  'g', ' ', 'i', 'e', '\'', 'n', 'e', 'r', 'n', 'r', 'n', 'd', ' ', ' ', ' ', ',', 'a', 'v', 'l', 'e', ' ', 'e', 'i', 't', 'f', 'r', ' ',
  'p', ' ', ' ', 't', 'o', 'r', ' ', 's', 'e', 'm', 'a', 'a', 'n', 'r', 'o', 'p', 'a', 'o', 'e', 'e', 'n', 'v', 'h', ' ', 'o', 'r', ' ',
  ' ', ' ', 'd', 'n', 'u', 'a', 'e', 'n', 'n', 'r', ' ', 'E', 'a', 'd', 'j', 'e', 'e', 'v', 'n', 'l', 'd', ' ', 'd', 'v', 'a', 'B', 'o',
  'n', 'o', ',', ' ', ' ', 'a', 'o', 'S', 'k', 'e', ' ', 'v', 'k', 'n', 'o', 'a', 'e', 'e', ' ', 'n', 'd', 't', 'o', 'k', ' ', ' ', 'e',
  'n', 't', 'm', 'j', 'r', 'i', 'w', 'e', 'd', 'n', 'v', 'n', 'd', 'a', 'i', ' ', ' ', 'a', 'e', 'd', 'b', 'r', ' ', 'B', ' ', ' '
]

def rotate_text(text, rot):
  string_new = ''
  for i in range(len(text)):
    pos = i*rot % len(text)
    string_new = string_new + text[pos]
  return string_new

def print_matrix(strng):
  for i in range(0, ceil(len(string)/27)):
    print(strng[i*27:i*27+27])
  print()

print_matrix(rotate_text(''.join(string), 1))

###
# Find the position of the apostrophe
print('--- \'S ---')
index_apos = string.index('\'')

# Find the positions of the S's and their rotation w.r.t. to the apostrophe
indexes_s = []
for i in range(0, len(string)):
  if string[i] == 's':
    indexes_s.append(i)
rotations = [x-index_apos for x in indexes_s]
print(index_apos, indexes_s, rotations)

# Rotate the text for all those rotations and 
for rot in rotations:
  print_matrix(rotate_text(string, rot))

###
# Find the dot
print('--- END DOT ---')
index_dot = string.index('.')

# Find the rotation that leads to having the dot at the end of th sentence
# 1 + rot * (num_chars - 1) = index_dot + N * num_chars (where N is an integer)
for N in range(len(string)):
  if (index_dot + N*len(string)) % (len(string)-1) == 0:
    rotation_dot = int((index_dot + N*len(string))/(len(string)-1))
    break
print(rotation_dot)
print_matrix(rotate_text(string, rotation_dot))


###
# What if the apostrophe should go after the s, to indicate posession?
print('--- S\' ---')
rotations = [index_apos-x for x in indexes_s]
print(index_apos, indexes_s, rotations)

# Rotate the text for all those rotations and 
for rot in rotations:
  print_matrix(rotate_text(string, rot))


###
# What if the string start at another capital?
# Find the positions of all uppercase letters
print('--- CAPS ---')
indexes_cap = []
for i in range(0, len(string)):
  if string[i].istitle():
    indexes_cap.append(i)
print(indexes_cap)

# Find the rotation that leads to having the dot at the end of th sentence
# index_cap + rot * (num_chars - 1) = index_dot + N * num_chars (where N is an integer)
# (index_cap + rot * (num_chars - 1)) % num_chars = index_dot 
rotations_cap = {}
for index_cap in indexes_cap:
  for rot in range(len(string)):
    if (index_cap + rot*(len(string) - 1) % len(string)) == index_dot:
      rotations_cap[index_cap] = rot
      break
print(rotations_cap)

# Rotate the text for all those rotations and print
for index, rot in rotations_cap.items():
  print_matrix(rotate_text(string[index:] + string[:index], rot))


### Try all rotations
print('--- ALL ---')
for i in range(1, len(string)):
  new_text = rotate_text(string, i)
  correct = 5
  for j in range(1, len(string)):
    if new_text[j] == ' ' and new_text[j-1] == ' ':
      correct -= 1
  #if correct > 0:
    #print(new_text)
print()

### Try an incrementing rotation
print('--- INCREMENT ROTATION ---')
position = 0
new_text = ''
for i in range(len(string)):
  position = (position + i) % len(string)
  new_text = new_text + string[position]
print_matrix(new_text)


### Try taking two letters at once
print('--- TWO AT ONCE ---')
old_text = ''.join(string)
new_text = ''
skip = 2
for i in range(len(old_text)):
  position_start = (skip*i) % len(old_text)
  position_end = (skip*(i+1)) % len(old_text)
  if position_end > position_start:
    new_text += old_text[position_start:position_end]
  else:
    new_text += old_text[position_start:len(string)] + old_text[0:position_end]
print_matrix(new_text)


### Get me the letterfrequencies
print('--- LETTER FREQUENCIES ---')
print({key: len(list(group)) for key, group in groupby(sorted(string))})
# Okay, the letterfrequencies look kind of normal

###
# What if it is 'T?
print('--- \'T ---')

# Find the positions of the Ts and their rotation w.r.t. to the apostrophe
indexes_t = []
for i in range(0, len(string)):
  if string[i] == 't':
    indexes_t.append(i)
rotations = [x-index_apos for x in indexes_t]
print(index_apos, indexes_t, rotations)

# Rotate the text for all those rotations and 
for rot in rotations:
  print_matrix(rotate_text(string, rot))


###
# What if it is 'N?
print('--- \'N ---')

# Find the positions of the Ns and their rotation w.r.t. to the apostrophe
indexes_n = []
for i in range(0, len(string)):
  if string[i] == 'n':
    indexes_n.append(i)
rotations = [x-index_apos for x in indexes_n]
print(index_apos, indexes_n, rotations)

# Rotate the text for all those rotations and 
for rot in rotations:
  print_matrix(rotate_text(string, rot))


### Try all rotations (no spaces aligning vertically)
print('--- ALL ---')
for i in range(1, len(string)):
  new_text = rotate_text(string, i)
  correct = 2
  for j in range(27, len(new_text)):
    if new_text[j] == ' ' and new_text[j-27] == ' ':
      correct -= 1
  if correct > 0:
    print_matrix(new_text)
print()


### Try all rotations (apostrophe above T)
print('--- ALL ---')
for i in range(1, len(string)):
  new_text = rotate_text(string, i)
  for j in range(27, len(new_text)):
    if new_text[j] == 't' and new_text[j-27] == '\'':
      print_matrix(new_text)


### Try all rotations (apostrophe under T)
print('--- ALL ---')
for i in range(1, len(string)):
  new_text = rotate_text(string, i)
  for j in range(27, len(new_text)):
    if new_text[j] == '\'' and new_text[j-27] == 't':
      print_matrix(new_text)


### Try all rotations (apostrophe diagonally from T)
print('--- ALL ---')
for i in range(1, len(string)):
  new_text = rotate_text(string, i)
  for j in range(28, len(new_text)):
    if new_text[j] == 't' and new_text[j-28] == '\'':
      print_matrix(new_text)

print(string.count(' '))
