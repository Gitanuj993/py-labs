# Nested dict as json file

d1 = { 1 : "AT" , 2 : { 201: "BT"},3 : "CT", 4 : { 301 : {300:"Okay"}}}
print(f" dict : {d1}")

# lets print "AT"
print(d1[1])

# print "BT"
print(d1[2][201])

# print "okay"
print(d1[4][301][300])
