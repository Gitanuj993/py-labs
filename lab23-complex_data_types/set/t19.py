s1 = { 45,56,67,90,46,67}
s2 = { 1,2,3,4}

print(f" s1 is subset of s2 : { s1.issubset(s2)}")
print(f" s2 is superset of s1 : {s2.issuperset(s1)}")
print(f" is s1 and s2 are disjoint : {s1.isdisjoint(s2)}") # different elements