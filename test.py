import json


with open('./templates/data.json', 'r') as f:
    a = json.load(f)

print(a)