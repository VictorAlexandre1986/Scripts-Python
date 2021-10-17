import os

caminho = r"C:\Users\Victor\Downloads"

lista_arquivos = os.listdir(caminho)

lista_datas=[]
for arquivo in lista_arquivos:
    #Quantidade de segundos, apartir da data referência do python,quanto maior o numero mais novo é
    data = os.path.getmtime(f'{caminho}\{arquivo}')
    #print(f'Arquivo : {arquivo} Data : {data}')
    lista_datas.append((data,arquivo ))
    
lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]
print(f'O ultimo arquivo atualizado {ultimo_arquivo[1]}')