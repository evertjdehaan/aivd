string = 'Voor de voet weg moet dit probleemveld worden neergetunneld in een motie, om langs deze weg in lijn met de afspraken met het cabinet al zwaluwstaartend de pijnpunten snelstens ten bestens af te concluderen'
string = string.lower().replace(' ', '')

def get_frequencies(strng):
  frequencies = {}
  for i in range(26):
    char = chr(i+ord('a'))
    frequencies[char] = strng.count(char)
  return frequencies

def print_analysis(orig, new):
  orig_freqs = get_frequencies(string.lower())
  freqs = get_frequencies(new.lower())
  total = 0
  rem_letters = ''
  for letter, freq in orig_freqs.items():
    diff = freq - freqs[letter]
    print(letter, diff)
    total += diff
    rem_letters += letter*diff
  print(total, rem_letters)

sentence = 'Lenstra wint geen goud geld door "de kerstpuzzel van Rivest, Shamir en Adleman" op te lossen, want de moeite wordt beloond met een luttele C USD.'
sentence2 = 'Arjen, twijfelend, weet actief een centen te vangen.'
sentence3 = 'De winst valt niet te rijmen met'

print_analysis(string, sentence+sentence2)
print()

print_analysis(sentence, sentence+sentence3)
print()

sentence = 'Lenstra wint geen goud geld door "de kerstpuzzel van Rivest, Shamir en Adleman" op te lossen, want de moeite wordt beloond met een luttele C USD. Arjens tijd.'

sentence = 'Lenstra won geen goud geld door de "kerstpuzzel" van Rivest, Shamir en Adleman op te lossen. C USD was de troost'

sentence = 'Een geniale Nederlander spotte een lammergier in de "kerstpuzzel" van Rivest, Shamir en Adleman. De winst? C USD.'

sentence = 'Lenstra kerstpuzzel Rivest, Shamir en Adleman code lammergier'
