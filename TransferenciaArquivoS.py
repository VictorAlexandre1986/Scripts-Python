import socket

ip_servidor='127.0.0.1'

porta=5000

conexao = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conexao.bind((ip_servidor,porta))

#Maximo de conexões em escuta
conexao.listen(10)

while True:
    sc,addr=conexao.accept()
    
    with open('recebido_oi.txt','wb') as arquivo:
        fim=0
        while(fim==0):
            #aloca no buffer o que foi recebido
            recebido = sc.recv(1024)
            
            #Enquanto tiver conteudo no arquivo 
            while(recebido):
                #Escreva do txt
                arquivo.write(recebido)
                
                #Aloca o resto no buffer
                recebido = sc.recv(1024)
                
                
                fim = 1

arquivo.close()
