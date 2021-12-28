import json

with open('abc.json','r') as file:
    d1_json = file.read()
    #transformando em dicionario
    d1_json = json.loads(d1_json)

for chave, valor in d1_json.items():
    print(chave)
    for k, v in valor.items():
        print(f'\t{k} {v}')