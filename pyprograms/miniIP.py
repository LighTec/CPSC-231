def miniIP(arg):
	for i in range(1, len(arg)):
		a = arg[:i]
		a = int(a)

		bc = arg[i:]
		for j in range(i, len(bc)):
			b = bc[:j]
			c = bc[j:]
			b = int(b)
			c = int(c)

			if(a < 256 and b < 256 and c < 256):
				print(a, '.', b, '.', c)
			else:
				Z = 1
				#print(a, '.', b, '.', c, '   IS NOT AN IP')
inp = input('')
miniIP(inp)
