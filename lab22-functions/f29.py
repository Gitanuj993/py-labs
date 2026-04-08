
#


def result(name,clg_name,*marks) : # positional arguements
    print(f" Name of student is : {name}")
    print(f" College name is : {clg_name}")
    print(f" marks are : [ {marks} ]")



result("AT","SDITS",1,2,3,4,5)
# name takes first arguements
# clg_name takes second arguement
# *marks takes all the remaining arguements
