# dict comprehension odd,even then prime

list_nums = [ x for x in range(1,5+1)]
print(f" list_nums: {list_nums}")
# Run
dict_even_odd = { i : "Even" if i % 2 == 0 else "odd" for i in list_nums}
print(f" dict_even_odd: {dict_even_odd}")
# Run
dict_even_odd2 = { i : "Odd" for i in list_nums if i % 2 != 0 }
print(f" dict_even_odd2: {dict_even_odd2}")

# Error
# dict_even_odd3 = { i : "Odd" for i in list_nums if i % 2 != 0 else "Even" }
# print(f" dict_even_odd3: {dict_even_odd3}")

# Error
# dict_even_odd4 = { i : "Odd" else "Even" for i in list_nums if i % 2 != 0 else "Even" }
# print(f" dict_even_odd3: {dict_even_odd4}")
#



