from crpt import Cryptography

strings = ['cdqiajneqgvajnkndwddqn', 'azczdfpjqcjndcscydcqfpjncd', 'cksioupcirkhhlpdnigglhrild', 'fmkcmtsfhgqpskkmqvcvcmgmnhgnsinchgnmomddscehdn', 'qmorlqditapofmqhcdah']
keys = ['Armando', 'Charles Aznavour', 'Koos Alberts', 'Montserrat Caballé', 'Queen of Soul']

crypt = Cryptography()
for string, key in zip(strings, keys):
  crypt.set_encoded_text(string)
  print(key, crypt.decode_monoalphabetic(key))
