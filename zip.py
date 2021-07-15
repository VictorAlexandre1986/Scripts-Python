from zipfile import ZipFile
import os

#Compactando os arquivos
caminho=r'C:/Users/Victor/Downloads/n64'
with ZipFile('arquivo.zip','w') as file:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho,arquivo)
        file.write(caminho_completo)

#Visualizando o conteudo do arquivo compactado
with ZipFile('arquivo.zip','r') as file:
    for arquivo in file.namelist():
        print(arquivo)
        
#Descompactando        
with ZipFile('arquivo.zip','r') as file:
    file.extractall('descompactado')