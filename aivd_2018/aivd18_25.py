from crpt import Cryptography

poem = 'Rgx hppeq hx fij gpiaij x Vpq cn jizij qppg qjob mxe Zx jifijmnobijcfq nqphkijc upi nqphkx Nqijcg upi nqxg iji ijce upi xe Fjjmappin zijq fij zijqqijm Fijzij x pgn c kgsn d Hppm cn bijq is ijiji gijqqijm Jt zxi bijq ijm qjob qvijij'

crypt = Cryptography()
crypt.set_encoded_text(poem)
keys = ['a', 'roerei', 'geklutst ei', 'omelet']
for key in keys:
  print(crypt.decode_vigenere(key))
  print()

frequencies = {}
for i in range(26):
  char = chr(i+ord('a'))
  frequencies[char] = poem.lower().count(char)
print(frequencies)
