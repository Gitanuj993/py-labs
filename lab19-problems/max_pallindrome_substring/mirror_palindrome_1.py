# finding max pallindrom substring from the string
s = input( " Enter sring : ")
max_pal = s[0] # there is a reason for it

def palindrom(s,low,high) : # even odd #	1,1, for odd , 1,2 for even
	global max_pal	
	for c in range(1,len(s) -1 ) :
		i = c - low
		j = c + high
		while ( i >= 0 and j < len(s)  and s[i] == s[j]) :
			len_pal = j - i + 1
				
			if len_pal >  len( max_pal) :
				max_pal = s[i:j+1:]
			i -= 1
			j += 1
		
																
# odd
palindrom(s,1,1)
#even
palindrom(s,1,2) # or 0,1
if len(s) <= 1 :
	print(" max pallindrom string is : ", s)
else :
	print("max pallindrom string is : ", max_pal)
	
