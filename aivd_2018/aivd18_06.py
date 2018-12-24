from crpt import Cryptography

signs = 'LB RO RB LB RO RB RO LB RB RO RO LB RB LB RB RO RO LB LB RB LB LB RB LB RB RO LB LO RO LB LB RB LB LO RO LB LB RB LB RB RO LB RB RO LB RO RB LB RO RO RB LB LB RB LB RO RO RO RB RO RO LB LB RB LB RB RO LB LO LB LB LB RO RB LB RO RB RO LB LO RO RO RB LB RB RO LB RB LB LB LB RB LB RB RO LB LO LB LB LB RO RB LB RB LB RO LB RB LB LB LB RB RO LB RO LB RB LB LB LB LB RB LB LB RB LB RO LB LB RB LB RO LB LB RB LB RB RO LB RB RO RO LB LB RO RO LO RO RO LB LB RB RO RO RO RB RO LB LB RB LB RO RB RO LB RB LB LB RB RO RO LB LO RO LB LB RB LB RO RB RO LO LB LB LB RB RO RO RO RB RO RO RB RO RO RB LB LB RB RO RO LB RB LB RB RO LB LO RO RO LB RB LB RB RO RO RB LB RO RB RO LB RO RB RO LB RO RB LB RB LB RO LB LB RB LB LB RB LB RO RO RO RB RO LB RO RB LB RB LB RO LB LO RO LB LB RB LB RO RB RO LB LO LB RO RB RO LB RB RO LB LB RB LB RB LB RO LB RB LB RB RO LB LO RO LB LB RB LB LO LB RB LB RB RO LB LO RO RO RO RB LB LB RO LB LO LB RO RB RO LB RB RO LB LB RB LB RB LB RO LB RB LB LO LB LB LB RO RB RO RO RO RB LB RO LB RB RO RO LO LB LB LB RO RB LB RO RB RO LB LO RO RO LB RB LB RB LB RO LB LB RB RO RO RO RB RO RO RO RB LB LB RO LB LO RO RO RO RB RO RO RB LB RO RB LB RO LB RB RO RO RB LB RB RO LB RB RO RO LB LB RO RO LO LB RO RO RB LB RO RB RO LB RB RO LO LB RO RO RB LB RO RB RO LO RO LB LB RB LB LO LB RB LB RB RO LB LO LB RO LB LB RB LB RB LB LB RB RO LB LB RB RO LO RO RB RO RO RO RB RO LO RO RO LB RB LB RB RO LB LB LB RB LB RB RO LB LB LO RO LB RO RB LB RO RB RO LB LO RO LB LB RB LB LO LB RO RB RO LB RB RO LB LB RB LB RB LB RO LB LO RO RB RO RO RO RB RO LO LB LB LB RB LB RO RO LB RB RO RO RO RB RO RB RO RB LB RB LB RO LB RB RO LB RB LB LB RB LB RO RO RO LO LB RO LB LB RB LB RB LB LB RB RO LB LB RB LB RB RO LB RB RO RO LB LB RO RO LO RO LB RO LB RB RO RO RO RB RO LB RB RO LB RO LB RB LB RO LB LB RB LB LB RO RB RO LB LB RB LB RB LB RB LB RO LB LO LB LB RB RO LB RO RB RO RO LB LB RO RO LO RO LB LB RB LB RO RB RO LO LB LB RB LB RB RO LB LB RB LB RB LB RO LB RB LB RB LB RB RO LB LO LB LB LB RO RB LB RO LB RB LB LB RB LB RO RO RO LO RO RO LB LB RB RO RO RO RB LB LB RO LO RO RO RB RO RO RO RB LB RB RO RB LB RB RO LB LO RO RO LB LB RB LB LB RB LB RO RO RO RB RO LB LO RO RO RO RB RO RO LO LB LB LB RO RB RO RO RO RB RO RO RO RB LB RO LB LO RO RO LB LB RB LB LB RB RO LB RO LB RB LB LB LB LB RB RO RO LB LB RB LB RB LB RO LB LB RB LB LB RO LB LO RO LB LB RB LB LO RO LB LB LB RB LB RO RB LB LB LB RB LB LB RB LB LB LB LO LB LB LB RO RB LB RO RB RO LB LO RO RO LB LB RB LB LB RB LB RO RO RO RB RO LB LO RO RO RO RB LB LB LB RO RB LB RB LB RO LB RB RO RB LB LB RO RB LB LB RB RO RO LB RB LB LB RB RO LB RB RO RO LB LO RO RB LB LO RO LB RO RB LB LB RB LB RB RO RO LB LB RB LB RB RO LB RB RO RO LB LB RO RO LO LB RB RO LB LO RO LB LB RB LB RO RB RO LO RO RO LB RB LB RB LB RO LB LB RB RO RO RO RB RO RO RO RB LB LB RO LB LO LB RO RB LB RO LB LB RB LB RO LB LB RB LB RB LB RB RO LB LO RO RO LB LB RB RO RO RO RB LB LB RO LO RO RO RB RO RO RO RB LB RB RO RB LB RB RO LB LO LB RO RO RB RO RO RO RB LB RO LB RB RO LB LB RB LB RB RO LB LO RO LB LB LB RB LB RB RO RO RO RB RO RO RO RB LB RO LB RB RO LB LB RB LB RB LB RB LB RO LB LB RB RO LB LB LO RO RO RO RB LB RO RO LB LO RO LB LB RB LB LO LB LB LB RO RB LB RO LB RB LB LB RO RB RO LB RO LB RB LB LB LB LB RB RO RB LB RB RO LB LO RO LB LB RB LB LB RB LB LO LB LB LB LB RB LB RB RO LO LB LB LB RO RB RO RO RO RB RO RO RO RB LB RO LB RB RO RB RO LB LB LB RB LB RO LB RB LB RB RO LB RB RO RO LB RB RO RB LB RO LB RO LB RO LO LB LB LB LB RB LB RB RO LO LB LB LB RO RB RO RO RO RB RO RO RO RB LB RO LB RB RO RB RO LB LB LB RB LB RO LB RB LB RB RO LB RB RO RO LB RB RO RB LB RO LB RO LB RO'

# Apply the morse signs
signs = signs.replace(' ', '')
signs = signs.replace('LB', '.')
signs = signs.replace('LO', ' ')
signs = signs.replace('RB', ' ')
signs = signs.replace('RO', '-')

# Decode morse letter by morse letter
crypt = Cryptography()
letters = signs.split(' ')
string = ''
for letter in letters:
  crypt.set_encoded_text(letter)
  decoded = crypt.decode_morse()
  if not decoded is None:
    string = string + crypt.decode_morse()

print(string)
