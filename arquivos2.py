import os
import shutil

caminhoOriginal = r'C:\Users\Victor\Desktop\Aprendendo\Vue'
caminhoNovo     = r'C:\Users\Victor\Desktop\Novo'

try:
    #Criando a pasta
    os.mkdir(caminhoNovo)
except FileExistsError as e:
    print(f'Pasta {caminhoNovo} já existe. ')
    
    
for raiz, diretorios, arquivos in os.walk(caminhoOriginal):
    for arquivo in arquivos:
        caminho_velho = os.path.join(raiz,arquivo)
        caminho_novo = os.path.join(caminhoNovo,arquivo)
        
        if '.jpg' in arquivo:
            shutil.move(caminho_velho,caminho_novo)
            print('Arquivos recortado e colado!!!')
    