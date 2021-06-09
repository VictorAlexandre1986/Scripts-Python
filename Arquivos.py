import os

caminho_procura = os.path.join('C:/Users/Victor/Desktop/Projetos/Forum')
termo_procurado = 'Cadastro.html'

def procurandoArquivo(caminho,arquivo):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if arquivo == termo_procurado :
                print(f'Arquivo encontrado :  {arquivo}')

def listarArquivos(caminho):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            print(f'{arquivo}')

def listarArquivos1(caminho):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz,arquivo)
            print(f'{caminho_completo}')
            
def listarArquivos2(caminho):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz,arquivo)
            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            print(f'Caminho : {nome_arquivo}  => Extensão : {extensao_arquivo}')            
            
def listarArquivos3(caminho):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz,arquivo)
            tamanho = os.path.getsize(caminho_completo)
            print(f'{arquivo}: {tamanho_arquivo(tamanho)}')
            
                        
def listarDiretorios(caminho):
    for raiz,diretorios,arquivos in os.walk(caminho_procura):
        for diretorio in diretorios:
            print(f'Diretorio encontrado : {diretorio}')

def qtdArquivos(caminho):
    contador = 0
    for raiz,diretorios,arquivos in os.walk(caminho_procura):        
        for arquivo in arquivos:
            contador+=1
    print(f'{contador} arquivos encontrados.')            
        
        
def tamanho_arquivo(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'    
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
      
    tamanho = round(tamanho,2 )
    return f'{tamanho}{texto}'.replace('.',',')  
        
                
try :            
    procurandoArquivo(caminho_procura,termo_procurado)
    listarArquivos3(caminho_procura)
    listarDiretorios(caminho_procura)
    qtdArquivos(caminho_procura)
except PermissionError as erro:
    print(erro)
except FileNotFoundError as erro:
    print(erro)