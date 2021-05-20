import os

#Verificando sistema operacional
print(f'Sistema operacional : {os.name}')

#Mudar o diretório
#os.chdir(path)

#Obtendo o path absoluto do arquivo em execução
print(f'Caminho atual : {os.getcwd()}')

#Não sei
print(os.fspath('C:/'))


#Nome do usuario logado
print(f'Nome do usuario logado é : {os.getlogin()}')


#Pid do processo atual
print(f'O id do processo atual é {os.getpid()}')

#Mostra todos os arquivos contidos dentro da pasta , retorna uma lista
print(f'Os arquivos da pasta são : {os.listdir("C:")}')


#Criando uma pasta
try:
    os.mkdir("C:/Teste")
except FileExistsError:
    print('A pasta já existe!!!')
    
    
#Função de criação recursiva de diretório
try:
    os.makedirs("C:/Teste/Testando")
except FileExistsError:
    print('Já existe essa sub-pasta')
    

#Chamando um comando externo
print(os.system("dir"))

#Verificando se um arquivo existe
print(os.path.isfile('C:/Teste/Testando/texto.txt'))

#Verificando se um diretprio existe
print(os.path.isdir('C:/Teste'))
    
#Removendo uma arquivo 
#print(os.remove('C:/Teste/Testando'))

#Removendo diretorio, remove os diretórios recursivamente
#print(os.removedirs('C:/Teste/Testando'))

#Remove o diretório
#print(os.rmdir('C:/Teste'))

#Renomeando
#print(f'Renomeando : {os.rename("src=C:/Teste/Testando/texto.txt","dst=C:/Teste/Testando/texto1.txt")}')