import requests 
import json
api_url = 'https://jsonplaceholder.typicode.com/todos'
todo={"usedId":1,'title':"Buy milk","completed":False}
headers = {"Content-Type":"application/json"}

reponse = requests.post(api_url, data=json.dump(todo),headers=headers)
reponse.json()

print(reponse.status_code)
