import json

with open('data2.json', 'r') as f:
    data = json.load(f)
print(len(data))