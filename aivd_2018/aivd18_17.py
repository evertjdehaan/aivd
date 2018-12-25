from crpt import Cryptography

rows = [['A','E','H','I','N','R','T','T','W','X','X','Z'],
['A','D','E','I','N','S','T','T','V','X','X','X'],
['D','E','J','M','N','O','R','T','T','X','X','X'],
['E','E','I','K','M','R','S','S','T','W','X','X'],
['D','D','E','O','O','P','R','R','T','X','X','X'],
['A','A','E','G','I','K','K','Q','R','R','S','Z'],
['C','F','H','L','M','M','Q','T','W','X','Y','Z'],
['A','A','C','F','H','Q','S','U','V','W','W','Y'],
['F','I','I','J','L','O','O','R','T','V','V','X'],
['A','C','F','G','H','I','J','L','O','Q','X','Y'],
['A','B','B','F','F','F','L','L','O','P','R','X'],
['E','E','I','I','O','Q','R','T','U','U','Z','Z'],
['G','I','K','N','P','T','U','V','V','V','X','Z']]
columns = [['A','F','I','I','I','J','K','L','R','S','X','X','Z'],
['B','D','D','E','I','J','M','N','O','Q','R','T','V'],
['C','F','H','I','K','M','R','T','X','X','X','X','Z'],
['A','H','H','J','N','O','S','T','U','U','V','X','X'],
['A','E','F','F','G','L','O','O','P','T','V','W','W'],
['A','E','F','M','M','N','O','P','Q','T','X','X','Z'],
['C','D','E','I','I','L','L','R','T','V','X','X','X'],
['A','D','E','G','G','O','R','S','S','T','U','Y','Z'],
['A','E','E','H','L','Q','T','W','X','X','Y','Z','Z'],
['A','A','I','N','O','Q','R','R','R','S','V','X','X'],
['F','K','K','O','P','Q','R','T','T','V','W','W','Y'],
['B','C','E','E','F','I','I','R','T','T','U','V','X']]

options = []
i = 0
for column in columns:
  string = ''
  for letter in column:
    if letter in rows[12]:
      string = string + letter.lower()
  options.append(''.join(sorted(list(set(string)))))
  i += 1

print(options)


crypt = Cryptography()
crypt.set_decoded_text('terdamse kraamzaal het kind Jacob Willem Katadreuffe met de sectio caesarea ter wereld geholpen'.lower().replace(' ', 'x'))
crypt.set_encoded_text('AIKAGQRSZRKEXMMTWZLYHQFCFQHUWACAYSWVIOIJFXVTLOVRXJCHLOIGQAYFLBFXFFLOARPBZRTUOEEUZIQIIVZNVPXGTVKU')
print(crypt.get_vigenere_key())
