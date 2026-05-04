# size of list
import sys

l1 = []  # 56

l2 = [ 1 ,2 ,3, 4,5 ,]

l3 = [True]

l4 = [None]

l5 = [ 1 , 1.4 , "AT" , None , False , print("AT")]



print(f" size of {l1} is : {sys.getsizeof(l1)}")
print(f" size of {l2} is : {sys.getsizeof(l2)}")
print(f" size of {l3} is : {sys.getsizeof(l3)}")
print(f" size of {l4} is : {sys.getsizeof(l4)}")
print(f" size of {l5} is : {sys.getsizeof(l5)}")

