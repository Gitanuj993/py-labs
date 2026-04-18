import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
# it prints status code
print(response.status_code)
# it prits json file
print(response.json())
# it prits json file
print(response.text)
