f = open("file5.txt","w",encoding="utf-8")
f.write("A")
print(" Tanwar",file=f) # file takes  file object not actual file name or not acutal file type
f.close()