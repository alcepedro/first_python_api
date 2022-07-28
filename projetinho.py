import requests
import json

def banana():
    print("olá")
    api = 'https://randomuser.me/api/'
    response = requests.get(api)
    print(response.json())
    

banana()




