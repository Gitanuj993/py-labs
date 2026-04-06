# pass 

use case :   passed or used a placeholder , we need a statement but we do not have to do any operations

- No action needed
- used to scale the program

```py
for i in range(5) :
    if i == 3 :
        #statements if provided
        pass
    print(i)
print("Done")

```

## pass used in database 


# continue 

- when we have to continue the loop 
- when we do not want to stop the loop at a condtions

```py
for i in range(10) :
    if i % 9 == 0 : # conditon become True 
        break
    if i == 6 :
        continue 
    if i == 2 :
        pass  
    print

```


# break 

- when require to stop the loop immeditely
- when we have to exit the loop
- Mostly used in while loop