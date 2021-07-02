import os
import shutil

caminho_velho = r'C:\Users\Victor\Downloads\n64'
caminho_novo =  r'C:\Users\Victor\Desktop\Copia'

def copiaArquivos():
    try:
        os.mkdir(caminho_novo)
    except FileExistsError as e:
        print(f'Pasta {caminho_novo} já existe. ')
        

    for raiz,diretorios,arquivos in os.walk(caminho_velho):
        for arquivo in arquivos:
            caminho_original = os.path.join(raiz,arquivo)
            caminho_copia = os.path.join(caminho_novo,arquivo)       
            print(arquivo)
            
            if 'z64' in arquivo:
                shutil.copy(caminho_original,caminho_copia)
                print(arquivo)                         
 
def copiaDiretorios():
    try:
        os.mkdir(caminho_novo)
    except FileExistsError as e:
        print(f'Pasta {caminho_novo} já existe. ') 

    
    shutil.copytree(caminho_velho,caminho_novo)  
            

copiaDiretorios()
