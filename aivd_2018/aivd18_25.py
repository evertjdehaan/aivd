from crpt import Cryptography
import getwords

poem = 'Rgx hppeq hx fij gpiaij x Vpq cn jizij qppg qjob mxe Zx jifijmnobijcfq nqphkijc upi nqphkx Nqijcg upi nqxg iji ijce upi xe Fjjmappin zijq fij zijqqijm Fijzij x pgn c kgsn d Hppm cn bijq is ijiji gijqqijm Jt zxi bijq ijm qjob qvijij'

crypt = Cryptography()
crypt.set_encoded_text(poem)
keys = ['a', 'roerei', 'geklutst ei', 'omelet', 'gemakkelijk', 'makkelijk', 'simpel', 'eenvoudig', 'eitje', 'ijtje']
for key in keys:
  print(crypt.decode_vigenere(key))
  print(crypt.decode_monoalphabetic(key))
  print()

frequencies = {}
for i in range(26):
  char = chr(i+ord('a'))
  frequencies[char] = poem.lower().count(char)
print(frequencies)
# Given the letter frequencies, it feels like it needs to be/can monoalphabetic. However, I cannot find all the words' signatures in the dictionary...

enc_dec = {'F': 'v', 'J': 'o', 'M': 'r', 'A': 'b', 'P': 'e', 'I': 'l'}
string = poem.upper()
for enc, dec in enc_dec.items():
  string = string.replace(enc, dec)
print(string)

### Let's try merging the I and J, since that might be the hint
poem = poem.replace('ij', 'y')
frequencies = {}
for i in range(26):
  char = chr(i+ord('a'))
  frequencies[char] = poem.lower().count(char)
print(frequencies)
print(poem)

print(getwords(pattern='jifymnobycfq'))
# Let's go for onderscheidt
enc_dec = {'J': 'o', 'I': 'n', 'F': 'd', 'Y': 'e', 'M': 'r', 'N': 's', 'O': 'c', 'B': 'h', 'C': 'i', 'Q': 't',
'Z': 'z', 'A': 'g', 'P': 'a', 'V': 'w', 'G': 'l', 'S': 'u', 'K': 'p', 'D': 'j', 'X': 'y', 'T': 'f', 'H': 'm', 'E': 'k', 'R': 'b', 'U': 'v'}
string = poem.upper()
for enc, dec in enc_dec.items():
  string = string.replace(enc, dec)
print(string)
