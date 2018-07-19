def donuts(count):
	if count >= 10:
		print('Number of donuts: many')
	else:
		print('Number of donuts: {}'.format(count))
		
def both_ends(s):
	if len(s) <= 2:
		print('')
	else:
	    print('{}{}{}{}'.format(s[0],s[1],s[-2],s[-1]))
	    
def fix_start(s):
	a = s[0]
	l = len(s)
	s = s.replace(a,"*")
	print(a+s[1:])

def mix_up(a,b):
	xa = a[:2] + b[2:]
	xb = b[:2] + a[2:]
	print(xb + ' ' + xa)	   
	    
	
	
	
	
	


