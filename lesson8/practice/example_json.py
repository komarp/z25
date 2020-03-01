import json

data = json.dumps({'key': 'value'})
print(data)

data = json.loads(data)
print(data)
