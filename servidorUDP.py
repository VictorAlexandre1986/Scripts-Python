import socket

meu_ip ='127.0.0.1'

minha_porta= 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

meu_servidor = (meu_ip, minha_porta)

#Fica escutando
udp.bind(meu_servidor)

while True:
    Msg_recebida, END_cliente = udp.recvfrom(1024)
    #recvfom(buffersize[, flags])deve ser um potencia de 2
    #Recebe dados de um soquete = um par (string, endereço), nde a string representa os dados recebidos

