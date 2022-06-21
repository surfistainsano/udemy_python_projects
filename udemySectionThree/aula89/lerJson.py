import json

with open('dict.json', 'r') as file:
    dictJson = file.read()  # retorna uma string
    dictJson = json.loads(dictJson)  # retorna um dict

for x, y in dictJson.items():
    print(x)
    for k1, v1 in y.items():
        print(k1, v1)
