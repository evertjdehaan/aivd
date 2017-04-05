WORDSPATH = "OpenTaal-210G-basis-gekeurd.txt"

def getwords(minlen = None, maxlen = None):
	corrchs = [chr(o) for o in range(ord("a"), ord("z")+1)]

	words = set()
	with open(WORDSPATH) as of:
		for line in of:
			word = line.strip().lower()
			if maxlen != None and len(word) > maxlen: continue
			if minlen != None and len(word) < minlen: continue

			for ch in word:
				if ch not in corrchs:
					break
			else: # if the loop didn't break, that is, if all characters are correct
				words.add(word)
	return words