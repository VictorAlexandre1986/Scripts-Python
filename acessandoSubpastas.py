import os

main_path='./Pasta'

for root,subfolder,archive in os.walk(main_path):
    for folder in subfolder:
        print(folder)
        
for root,subfolder,archives in os.walk(main_path):
    for archive in archives:
        print(archive)

#Pegando o camiho absoluto da pasta atual        
print(os.path.abspath('.'))

#Formando um caminho
print(os.path.join('pasta','subpasta','nome_arquivo'))

#Comandos do SO
lista=os.system('dir')
for item in lista:
    print(item)

