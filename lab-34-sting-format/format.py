#	string formating rituals 

# str.format(<val>) just like str.upper()

name = "Anuj"
marks = 90
# single value
print("Welcome {} !",format(name))
print("Welcome {} !".format(name))
# .formate() simple , position wise
print("{} has scored {} out of 100 in maths olympiad".format(name,marks) )
# .format() now index wise
print("{1} is learning {0} by consistently practicing and improving !".format('python',name))

# practice it 
print(" {0} {0} {1}".format('Hi',name) )

	

print("="*100)
print("center alignment ")	
print('{:*^10}'.format(name))
print( ' {:^10} welcome '.format('name')) 
print( " left alignment : " )
print( " {:<10} left alignment".format(name))
print("Right alignment : ")
print(" {:>10} right alignment".format(name))

print( "floating point values : ") 
PI = 3.1415
print( f" PI : {PI} " )
print(" After 2 decimal precision ")
print(" PI is : {: .2f} ".format(PI))







#left alignments
#print("{: < 10} have a seat ".format(name)) # error : spaces not allowed
#print("{ : <10} have a seat ".format(name)) # error : spaces not allowed in before ':' and after "<"
#print(f" {name : ^10}")
#print( ' {: ^10 } welcome '.format('name'))

