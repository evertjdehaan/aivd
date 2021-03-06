from itertools import groupby
from crpt import Cryptography

signs = ['00110', '11001', '10000', '10110', '00001', '11110', '01111', '00010', '11011', '10000', '10100', '10101', '00010', '00010', '01111', '10100', '10000', '00110', '11110', '10000', '11100', '00001', '00001', '01111', '10100', '00010', '11011', '00010', '11110', '10001', '10000', '00010', '11100', '10000', '11001', '00111', '11010', '00010', '11110', '10000', '10101', '00010', '11011', '11001', '00010', '11110', '10100', '10000', '01001', '00111', '11110', '01010', '00010', '11011', '00101', '00110', '10000', '01111', '00110', '00010', '10000', '10011', '00010', '01010', '01010', '00010', '11110', '10001', '10000', '00101', '10000', '11010', '00001', '00001', '11001', '10101', '10000', '00111', '00111', '11001', '10000', '11111', '00111', '11111', '00001', '11100', '10101', '10001', '10000', '00110', '11001', '10000', '10110', '00010', '00010', '10101', '10000', '01011', '00010', '11011', '00010', '11010', '00001', '00001', '11011', '10000', '11110', '00110', '00010', '10101', '10000', '10110', '00001', '10101', '10000', '01111', '00001', '10101', '10000', '00110', '10100', '10001', '10000', '11111', '00111', '11111', '00001', '11100', '10101', '10001', '10000', '01111', '00110', '10101', '10000', '10110', '00010', '11100', '11001', '10000', '11010', '00001', '00001', '11001', '10000', '00110', '11001', '10000', '00001', '11011', '10000', '01111', '00010', '11100', '10101', '00110', '01010', '10000', '01001', '00001', '00001', '11100', '10001']

# Get a frequency analysis of each of the options
print({key: len(list(group)) for key, group in groupby(sorted(signs))})

# Get a frequency analysis of two-character groups
two_chars = []
for i in range(1, len(signs)):
  two_chars.append(signs[i-1] + signs[i])
#print({key: len(list(group)) for key, group in groupby(sorted(two_chars))})

# Get a frequency analysis of two-character groups
three_chars = []
for i in range(2, len(signs)):
  three_chars.append(signs[i-2] + signs[i-1] + signs[i])
#print({key: len(list(group)) for key, group in groupby(sorted(three_chars))})

# Print the number series
strng = ''
for x in signs:
  strng = strng + str(int(x, 2)) + ' '
print(strng)

# Decode it with Baudot
full_string = ''.join(signs)
crypt = Cryptography()
crypt.set_encoded_text(full_string)
print(crypt.decode_baudot())


signs = ['01001', '11100', '00100', '10010', '11100', '10000', '11110', '01011', '01010', '11100', '01011', '00010', '10000', '00110', '11100', '00010', '00111', '10111', '00001', '11101', '01010', '10000', '01100', '00001', '11101', '11100', '00010', '11101', '11100', '00100', '11100', '00001', '10000', '11110', '10000', '00111', '10000', '11100', '00001', '10000', '11111']

# Decode it with Baudot
full_string = ''.join(signs)
crypt = Cryptography()
crypt.set_encoded_text(full_string)
print(crypt.decode_baudot())
print(crypt.decode_baudot('lsb'))

# The first result makes way more sense than the second..., but it is no useful text yet...
crypt.set_encoded_text(crypt.decode_baudot())

for i in range(26):
  print(i, crypt.decode_rotation(i))
