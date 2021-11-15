import requests 
api_url = 'https://jsonplaceholder.typicode.com/todos'
todo={"usedId":1,'title':"Buy milk","completed":True}
reponse = requests.post(api_url, json=todo)
reponse.json()

print(reponse.status_code)
