# dict.update(<iterable>)
std1 = {
    1: "Aarav",
    2: "Vivaan",
    3: "Aditya",
    4: "Vihaan"
}

print(f" std1 : {std1}")

std2 = {
    5: "Arjun",
    6: "Sai",
    7: "Reyansh",
    8: "Krishna"
}
print(f" std2 : {std2}")

# how can we update std1 with std2

list1 = [ (  5 ,"Arjun"),( 6 ,"Sai"),( 7 ,"Reyansh"),(8, "Krishna")]
print(f" list1 : {list1}")
std3 = std1.update(list1) # added to the original one

# mapped updated dict
print(f" std3 : {std3}") # None
print(f" std1 : { std1}")

