sentence = 'noll hu tonde tonko noll tonko tonde tongo de de go tonde tonko me la tonko ra go tonti tonko hu go tonsu go la tonko me tonde tonhu tonko ti noll la tonko tonde tonti noll noll tonti tonko noll tonko by go hu me ni ko tonko noll noll la tonko tonra tonko fy hu tongo tonde tonko tonme tonko fy hu tongo tonde tonko tonni tonvy tonko tonby go tonan ko tonko me tonde tonko tonra tonhu tonko tonme tonko me tonde tonko tonde fy go hu tonko go la tonko tonni tonko me tonde tonko ni go tonko vy po la ti tonko ti me de ra tonti tonko ra po tongo ti go la tonvy'
words = sentence.split(' ')

# The words are all in the tonal counting system (http://unifoundry.com/tonal/)
counting = {'noll': 0, 'an': 1, 'de': 2, 'ti': 3, 'go': 4, 'su': 5, 'by': 6, 'ra': 7, 'me': 8, 'ni': 9, 'ko': 10, 'hu': 11, 'vy': 12, 'la': 13,  'po': 14, 'fy': 15,'ton': 16, 'tonan': 17, 'tonde': 18, 'tonti': 19, 'tongo': 20, 'tonsu': 21, 'tonby': 22, 'tonra': 23, 'tonme': 24, 'tonni': 25, 'tonko': 26, 'tonhu': 27, 'tonvy': 28, 'tonla': 29, 'tonpo': 30, 'tonfy': 31}

# What if the number indicates an increment from the letter a?
string = ''
for word in words:
  string = string + chr(65 + counting[word])

print(string)
