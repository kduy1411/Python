import requests 
api_url ="https://jsonplaceholder.typicode.com/todos/1"
reponse = requests.get(api_url)
print(reponse.status_code)
print(reponse.json())
