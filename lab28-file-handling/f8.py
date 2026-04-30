
with open("f8.txt",'r+',encoding="utf-8") as f :
    data = f.read()
    f.write(" this read and write mode ")
    
    print(data)

