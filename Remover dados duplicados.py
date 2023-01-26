from typing import Dict

lista = (5, 5, 4, 4, 2, 2, 3, 3, 3, 1, 0, 0, 1, 5)

#Removendo se a ordem não importa
Removendo= list(set(lista))
print(Removendo)


#Removendo se a ordem importa
Removendo2= list(dict.fromkeys(lista))
print(Removendo2)

def remover_dados_duplicados_de_lista(lista):
    lista_sem_duplicados = []
    for item in lista:
        if item not in lista_sem_duplicados:
            lista_sem_duplicados.append(item)

    return lista_sem_duplicados

x = remover_dados_duplicados_de_lista(lista)
print(x)


dicionario ={"a":1,"a":2,"b":3,"c":4,"b":10}

def remover_dados_duplicados_de_dicionario(dicionario: Dict)-> Dict:
    dicionario_sem_duplicado = dict()
    for chave, valor in dicionario.items():
        if dicionario[chave] not in dicionario_sem_duplicado:
            #dicionario_sem_duplicado = dicionario_sem_duplicado.update({chave: valor})
            dicionario_sem_duplicado = dicionario[chave] = valor

    return dicionario_sem_duplicado

y = remover_dados_duplicados_de_dicionario(dicionario)
print(y)

#Se for uma tabela
#pip install pandas numpy openpyxl

#import pandas as pd

#produtos = pd.read_csv("Produtos.csv", sep=";")
#produtos = produtos.drop_duplicates(keep="first") #Remove o item onde todas as colunas são duplicadas
#produtos2 = produtos.drop_duplicates("Produto") #Remove os duplicados baseado na coluna produto
#produtos3 = produtos.drop_duplicates(["Produtos","Preco"]) #Remove os duplicados baseado nas duas colunas, mas poderia ser mais
#print(produtos)

