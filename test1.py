import requests
import substr
import json
response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
response1 = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
response = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
json_response = response.json()+response1.json()
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
print(dictionary)
