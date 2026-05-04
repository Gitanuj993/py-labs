# map(f,x)  : is a functions 

### map(f,x) is a funcrion which takes first function or lambda function as an first argument and
### seconds parameter as an iterable.

map(f,x) perform operations of function 'f' on elements of iterable 'x' one by one
map(f,x) returns an iterator object reference , 
we can convert the result into list(), tuple() or any other as per requirement



# map(f,x) used in following projects.
 # 🗺️ Python `map()` Function – In-Depth Guide

## 🎯 Purpose
`map()` is used to **transform each element of an iterable** using a function.

Instead of:
> “Keep some values” (filter)

It does:
> “Apply a function to every value”

---

## 🧠 What is `map(f, x)`?

### Syntax:
```python
map(function, iterable)
```

### Meaning:
- `function (f)` → transformation logic
- `iterable (x)` → list, tuple, etc.

### Returns:
- A **map object (iterator)** with transformed values

---

## ⚙️ How It Works Internally

For each element:
```python
new_value = function(element)
```

---

## 🧪 Example

```python
nums = [1, 2, 3, 4]

def square(n):
    return n * n

result = map(square, nums)

print(list(result))  # [1, 4, 9, 16]
```

---

## 🔄 Equivalent Using Loop

```python
result = []
for n in nums:
    result.append(n * n)
```

👉 `map()` replaces this pattern.

---

## ⚡ Using Lambda (Most Common)

```python
nums = [1, 2, 3]

result = list(map(lambda x: x * 2, nums))

print(result)  # [2, 4, 6]
```

---

## 🔁 Multiple Iterables

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))

print(result)  # [5, 7, 9]
```

👉 Stops at shortest iterable.

---

# 🎓 Learning Use Cases

## 1. Square Numbers
```python
list(map(lambda x: x*x, nums))
```

---

## 2. Convert Strings to Integers
```python
nums = ["1", "2", "3"]
list(map(int, nums))
```

---

## 3. Convert to Uppercase
```python
names = ["anuj", "rahul"]
list(map(str.upper, names))
```

---

## 4. Add Constant Value
```python
list(map(lambda x: x + 10, nums))
```

---

## 5. Length of Strings
```python
list(map(len, ["hi", "hello"]))
```

---

## 6. Boolean Mapping
```python
list(map(lambda x: x > 2, nums))
```

---

# 🌍 Real-World Use Cases

## 1. Data Transformation (APIs)
```python
ids = map(lambda user: user["id"], users)
```

---

## 2. Data Cleaning
```python
clean = map(str.strip, raw_data)
```

---

## 3. Financial Calculations
```python
taxed = map(lambda x: x * 1.18, prices)
```

---

## 4. Batch Processing
```python
results = map(process_function, data)
```

---

## 5. Formatting Output
```python
formatted = map(lambda x: f"₹{x}", amounts)
```

---

## 6. Feature Engineering (ML)
```python
normalized = map(lambda x: x/100, scores)
```

---

# ⚠️ Common Mistakes

- Forgetting `list()`:
```python
print(map(...))  # ❌ useless object
```

- Overusing lambda → unreadable code

- Using `map()` when list comprehension is clearer:
```python
[x*x for x in nums]  # often better
```

---

# 🧪 “Looks Illegal but Works” Programs

Because Python doesn’t care about your expectations.

---

## 1. Function Returning Boolean

```python
nums = [1, 2, 3]

print(list(map(lambda x: x > 1, nums)))
```

### Output:
```
[False, True, True]
```

👉 You’re mapping to booleans, not filtering.

---

## 2. Mapping with `None` Function

```python
nums = [1, 2, 3]

print(list(map(None, nums)))
```

### ❌ Error in Python 3:
```
TypeError
```

👉 Worked in Python 2, not anymore.

---

## 3. Side Effects Only (Weird Usage)

```python
nums = [1, 2, 3]

list(map(print, nums))
```

### Output:
```
1
2
3
```

👉 Returns `[None, None, None]`

Why?
- `print()` returns `None`

---

# ⚖️ `map()` vs Alternatives

| Use Case | Prefer |
|--------|--------|
| Simple transformation | list comprehension |
| Reusable function | map() |
| Multiple iterables | map() |
| Readability priority | loop |

---

# 🧩 Final Thought

`map()` is just:
> “Apply function to every element”

Nothing magical.

Use it when:
- It simplifies logic  
Avoid it when:
- It turns your code into a puzzle

Readable code wins. Always.
