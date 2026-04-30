#	map() used to extract data from the api

data = [ { "name" : "Anuj" , "id" :101} , { "name" : "Ankit" , "id" : 102 } ]
print(data)
user_names = list( map( lambda user : user["name"] , data ))
print(user_names)
