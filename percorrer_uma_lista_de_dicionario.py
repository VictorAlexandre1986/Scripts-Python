# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
lista = [
    {"nome":"Victor"},
    {"nome":"Xispita"},
    {"nome":"Shakira"},
    {"nome":"Nenem"},
    {"nome":"Negona"},
    {"nome":"Neguinha"},
    {"nome":"Peta"},
    {"nome":"Branca"},
    {"nome":"Fifi"}
]

def Percorrer(lista):
    for item in lista:
        print(item['nome'])

def outraManeira(lista):
    nomes = [nome['nome'] for nome in lista]
    return nomes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nomes = outraManeira(lista)
    for nome in nomes:
        print(nome)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
