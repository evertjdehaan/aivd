def print_chars(*args):
  # Print the letters matching the values, surrounded by known text
  string = 'een'
  for arg in args:
    string = string + chr(64+arg)
  print(string+'..gaf')

# Find all possibilityies for the four-level pyramid with the d in it
char8 = 4
for char0 in range(1, 27):
  for char1 in range(1, 27):
    char2 = char0 - char1
    if char2 < 1:
      continue
    for char3 in range(1, 27):
      char4 = char1 - char3
      if char4 < 1:
        continue
      char5 = char2 - char4
      if char5 < 1:
        continue
      char9 = char5 - char8
      if char9 < 1:
        continue
      char7 = char4 - char8
      if char7 < 1:
        continue
      char6 = char3 - char7
      if char6 < 1:
        continue
      print_chars(char0, char1, char2, char3, char4, char5, char6, char7, char8, char9)
