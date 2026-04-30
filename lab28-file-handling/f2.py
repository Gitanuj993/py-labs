
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
with open("test.txt",encoding="utf-8") as file :
    data = file.read()

    print(data)