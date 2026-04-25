# This file name
print(__name__)

# This will run module t2 if
import t2

res = t2.t1.add(1,3)
print(res)
# res = t1.add(1,3) # NameError: name 't1' is not defined. Did you mean: 't2'?
