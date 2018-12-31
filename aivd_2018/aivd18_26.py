from crpt import Cryptography

words = ['GEESTELIJK', 'ONGEWIJD', 'MACHTIG', 'WEERGEKOMEN', 'STER', 'WERKELIJK', 'KINDJE', 'BUITEN', 'KNUFFELEN', 'KONIJN', 'LICHTBUNDEL', 'ENGELTJE', 'KUNSTIG', 'PLASTISCH', 'HAASTEN', 'WINDSNELHEID', 'WEERLEGGEN', 'DUVEL', 'ACHTER', 'FORMALISEREN', 'VLOEIEND', 'KOSTELIJK', 'STAPPEN', 'LUISTER', 'REKENING', 'DONDER', 'STAGE', 'VERDER', 'FINEREN', 'FIER', 'ONBEGREPEN', 'AANDACHTIG', 'ZINDELIJK', 'RESTJE', 'RECEPTIE', 'WOORDELIJKE', 'ONTERING', 'LALA', 'OTTER', 'WERF', 'BRUI', 'EMMERS', 'MISERES', 'GETTO']

string = ''
for word in words:
  string += word[0]

crypt = Cryptography()
crypt.set_encoded_text(string)

for i in range(26):
  print(i, crypt.decode_rotation(i))

string = ''.join(words)
print(len(string))
for i in range(1, 50):
  prnt = ''
  for j in range(0, len(string), i):
    prnt += string[j]
  print(prnt)
