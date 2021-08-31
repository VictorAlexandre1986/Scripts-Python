#pip install pywin32  
import win32print
import win32api
import os


#escolher a impressora
lista_impressoras=win32print.EnumPrinters(2)
for impressora in lista_impressoras:
    print (impressora) 
    
# Escolhendo a impressora
impressora = lista_impressoras[4]

#definindo
win32print.setDefaultPrinter(impressora[2])

#mandar imprimir
#O caminho deve informar até a pasta com os arquivos a serem impressos,não o arquivo em si
caminho=r'caminho'
lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
    #ShellExecute roda um comando dentro do windows
    win32api.ShellExecute(0,'print',arquivo,None,caminho,0)
    
    
#Caso haja um erro verifique se possui um leitor de pdf instalado no computador,não pode ser
#um browser