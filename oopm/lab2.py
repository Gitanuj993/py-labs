""""
Welcome AT
lab2
aim : encapsulation in pythom
"""
class base :
	data = None 
	def __init__(self) :
		print(" Object is created !")
	def show_data(self) :
		print("   ", self.data)
		
		
		
		
		
		
if __name__ == "__main__" :
	
	obj = base()
	obj.data = 100 
	obj.show_data()
	
	