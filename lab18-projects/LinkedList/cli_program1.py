# new function to impliment linked list using classes in python.

class Node :
	def __init__( self , val = 0 , next = None ) :
		self.val = val 
		self.next = None
		
class LinkedList :
	def __init__(self) :
		self.head = None
		
	def create_linked_list(self) :
		try :
			value = int(input("Enter value : ")) 
		except Exception as e :
			print("Please enter a valid number ! ")
		else :
			 new_node = Node(value)
		
		if  self.head == None :
			self.head = new_node
		else :
			# lets find the end node
			temp = self.head
			while ( temp.next != None ) :
				temp = temp.next
			# after reaching a last node we will  add new node at the end
			temp.next = new_node
			# node created successfully
		
		
	def display_linked_list(self) :
		# initializing self.head value in a temp
		temp = self.head
		while temp is not None :
			print( temp.val , " -> " , end = " " )		
			temp = temp.next
		# at the end lets print None
		print(None)
		

if __name__ == '__main__' :
	s = LinkedList()
	while True :
		print("Choose from the following !. ")
		print(" 1. To create a new list " )
		print(" 2.To insert an element at the end ")
		print(" 3. To display the linked list ")
		print(" 6. To exit the program ")
		print() 		
		choice = None
		try :
			choice = int(input("Enter your choice : "))
			
		except Exception :
			print("Enter valid choice !",e) 			
		#	lets take the decision
		if choice == 1 :
			 s.create_linked_list()
		elif choice == 2 :
			 s.create_linked_list()
		elif choice == 3 :
			 s.display_linked_list()
		elif choice ==6 :
			 print(" Thanks for using our service !") 
			 break
		else :
			 print("Enter valid choice : ")
