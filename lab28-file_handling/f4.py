with open("file4.txt","w",encoding="utf-8") as f :
    pass

with open("file4.txt","r",encoding='UTF-8') as f :
    f.writelines("Welcome To The files \n")
    print("You can also write here and send it to the file",file=file4)
