from crpt import Cryptography

crypt = Cryptography()
crypt.set_encoded_text('emokrytrtjnidntgvqumvdasxxrjkfuhranjnhrcrgdnofrwnsdynffwlpwsykxxoorqzeuwyy')
keys = ['rob bertholee', 'tot ziens', 'auf wiedersehen', 'au revoir']

for key in keys:
  print(crypt.decode_atbash())
  print(crypt.decode_bifid(key))
  print(crypt.decode_monoalphabetic(key))
  print(crypt.decode_playfair(key))
  for i in range(2,10):
    print(crypt.decode_rail_fence(i))
  print(crypt.decode_vigenere(key))
