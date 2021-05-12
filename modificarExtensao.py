import os

caminho = r'C:\Users\Victor\Downloads'

print('O caminho dos arquivos é {}'.format(caminho))

extensao_velha = '.' + input("Imforme a extensão a ser substituida : ")
extensao_nova = '.' + input("Informe a extensão nova : ")

contador_arquivos = 0

with os.scandir(caminho) as arquivos:
    for arquivo in arquivos:
        if arquivo.is_file():
           caminho,extensao = os.path.splitext((arquivo.path))
           if extensao == extensao_velha:
               novo = caminho + extensao_nova
               os.rename(arquivo.path, novo)
               contador_arquivos+=1

print('Finalizado!!!')
print(f'O numero de arquivos modificados é {contador_arquivos}')
print(f'Os arquivos foram modificados da extensão {extensao_velha} para {extensao_nova}')