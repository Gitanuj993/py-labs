 # linked list in python
 
 # list node
class ListNode :
 		def __init__(self,val = 0 ,next = None) :
 			self.val = val 
 			self.next = next
 
 # linked list
class LinkedList :
 	def __init__(self) :
 		self.head = None
 	
 	def create(self) :
 		val = int(input("Enter value : "))
 		new_node = ListNode(val)
 		if ( self.head == None) : 			 			
 			self.head = new_node
 			print(" new head is created :",self.head.val)
 		else :
 			temp = self.head
 			while(temp.next != None) :
 				temp =temp.next
 			temp.next = new_node 			 			 			 			
 			temp = temp.next 			
 			print(" element is created in the linked list ", temp.val)
 	#	return head 
 	def show(self) :
 			print(" show function is there")
 			temp = self.head
 			print("temp.value is : left : ",temp.val)
 			print("Initial value of temp object  is ",temp) 
 			# now traversing the linked list
 			while ( temp is not  None) :
 				print(f" {temp.val} -> ",end =" ")
 				temp = temp.next
 			#print("temp.value is : left : ",temp.val)
 	 	
if __name__ == '__main__' :
 		s = LinkedList()
 		s.create( )
 		s.create( )
 		s.create()
 		s.show( )
 		
 	
