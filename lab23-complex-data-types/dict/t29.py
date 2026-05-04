d = {
    "A": 10,
    "B": {
        "B1": 20,
        "B2": {
            "B21": "Python",
            "B22": "Java"
        }
    },
    "C": {
        "C1": {
            "C11": 100
        },
        "C2": "Coding"
    }
}

# 1. Print value of "A" = 10
print(d["A"])

# 2. Print value of "B1" = 20
print(d["B"]["B1"])
# 3. Print "Python"
print(d["B"]["B2"]["B21"])
# 3. Print "Python"
print(d["B"]["B2"]["B22"])

# 5. Print 100
print(d["C"]["C1"]["C11"])

# 6. Print "Coding"
print(d["C"]["C2"])
# 6. Print d of "Coding"
print(d["C"]["C2"][2])

