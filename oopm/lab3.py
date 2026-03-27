"""
Welcome AT
lab3
aim : inheritance : using property of one class into another class 
	we make a program showing single level inheritance
"""

class base :
	
	def info(self) :
		print(" I am the base class ! ")
		
		
class child(base) :
	pass
	
	
if __name__ == "__main__" :
	obj = child()
	