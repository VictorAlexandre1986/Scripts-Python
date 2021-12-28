import json

d1 = {
    'Pessoa 1':{
        'nome':'Victor',
        'idade':35
    },
    'Pessoa 2':{
        'nome':'Xispita',
        'idade':10
    }
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)