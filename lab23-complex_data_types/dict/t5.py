# what happen if  we provide only one element
testList2 = [ (1,),(2,),(3,),(4),(5,) ] # dictionary update sequence
print(f" testList2: {testList2}")
dict2 = dict(testList2)
print(f" dict2: {dict2}")
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

