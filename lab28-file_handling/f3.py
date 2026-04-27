try :
    with open("new.txt","w",encoding="utf-8") as file :
        data = file.write("Welcome to the files !")
except Exception("nothing") as e :
    print(e)

print(data)