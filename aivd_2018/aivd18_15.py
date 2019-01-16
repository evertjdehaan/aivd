from crpt import Cryptography

crypt = Cryptography()
crypt.set_encoded_text('emokrytrtjnidntgvqumvdasxxrjkfuhranjnhrcrgdnofrwnsdynffwlpwsykxxoorqzeuwyy')
#keys = ['rob bertholee', 'tot ziens', 'auf wiedersehen', 'au revoir', 'eunice gayson', 'dj hardwell', 'oudejaarsconference', 'oudjaarsconference', 'eindejaarsconference', 'eindjaarsconference', 'toptweeduizend', 'tweeduizendachtien', 'eurovisiesongfestival', 'elfstedentocht', 'elfstedenzwemtocht', 'eerste wereldoorlog', 'early man', 'escobar', 'Last Goodbye', 'No Good In Goodbye', 'Goodbye Stranger', 'Beautiful Goodbye', 'Goodbye My Lover', 'Time To Say Goodbye Con Te Partirò', 'Sweet Goodbyes', 'een afscheid', 'een afscheid met een ingebouwde terugblik', 'emeritaat', 'saluut', 'afzwaai', 'vertrek', 'groeten', 'ontslag', 'bedankje', 'adieu', 'ajuus', 'scheiding', 'uitgeleide', 'echtscheiding', 'vertrek', 'flashback', 'beschouwing', 'retrospectie', 'reflectie', 'edwin evers', 'evers staat op', 'Geniet van alles gun elkaar wat en wat mij betreft graag tot snel', 'een restart met een kleine tussenpauze', 'weet je het zeker', 'vreemde wegen', 'Het ware prachtige bijzondere indrukwekkende en vaak ook vreemde wegen die mij brachten tot hier', 'herdenkinksbijeenkomst wim kok', 'marathonuitzending', 'afscheid edwin evers', 'We gaan er gewoon een leuke dag van maken We gaan een klein beetje terugblikken en niet te sentimenteel doen', 'We gaan een klein beetje terugblikken en niet te sentimenteel doen', 'afscheidsuitzending', 'afscheidsuitzending edwin evers']
keys = []

#print(crypt.decode_atbash())
#for i in range(2,10):
#  print(crypt.decode_rail_fence(i))
for key in keys:
  print(crypt.decode_bifid(key))
  print(crypt.decode_playfair(key))
  print(crypt.decode_vigenere(key))
#for key in keys:
#  print(crypt.decode_bifid(key[::-1]))
#  print(crypt.decode_playfair(key[::-1]))
#  print(crypt.decode_vigenere(key[::-1]))

plains = ['edwin evers', 'evers staat op', 'Geniet van alles gun elkaar wat en wat mij betreft graag tot snel', 'een restart met een kleine tussenpauze', 'weet je het zeker', 'vreemde wegen', 'Het ware prachtige bijzondere indrukwekkende en vaak ook vreemde wegen die mij brachten tot hier', 'herdenkinksbijeenkomst wim kok', 'marathonuitzending', 'afscheid edwin evers', 'We gaan er gewoon een leuke dag van maken We gaan een klein beetje terugblikken en niet te sentimenteel doen', 'We gaan een klein beetje terugblikken en niet te sentimenteel doen', 'afscheidsuitzending', 'afscheidsuitzending edwin evers']

for plain in plains:
  filler = 'a'*len('emokrytrtjnidntgvqumvdasxxrjkfuhranjnhrcrgdnofrwnsdynffwlpwsykxxoorqzeuwyy')
  string = plain.replace(' ', '')
  string = string[:len(filler)]
  encoded = string + filler[len(string):]
  crypt.set_decoded_text(encoded)
  print(crypt.get_vigenere_key())
