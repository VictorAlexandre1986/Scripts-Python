import socket

ip_servidor='127.0.0.1'

porta=5000

conexao = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conexao.connect((ip_servidor,porta))

with open ('arquivo.txt','rb') as arquivo:
    #le e armazena no buffer
    memoria = arquivo.read(1024)
    
    while(memoria):
        
        #Enviando para o servidor
        conexao.send(memoria)
        
        memoria = arquivo.read(1024)

conexao.close()
        