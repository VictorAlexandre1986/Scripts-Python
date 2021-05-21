import socket

meu_ip='127.0.0.1'

porta=8000

#Sock_stream é tcp
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

destino = (meu_ip, porta)

tcp.connect(destino)

while True:
    msg = input('Entre com a mensagem')
    
    #(bytes(msg,utf8)) = Converte str para byte
    tcp.send(bytes(msg,'utf8'))
    
    
#finaliza o socket    
tcp.close()
