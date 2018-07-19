def match_ends(words):
	x = 0
	for i in words:
		if len(i) >= 2 and i[0] == i[-1]:
			x += 1
	return x

def front_x(words):
	a = []
	b = []
	for x in words:
		if x[0] == 'x':
			a.append(x)
		else:
			b.append(x)
	print(sorted(a)+sorted(b))
	
	
def last(a):
	return a[-1]
def sort_last(tuples):
	return sorted(tuples, key=last)
	
	
		
