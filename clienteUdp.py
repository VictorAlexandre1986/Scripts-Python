import socket

ip_servidor = '127.0.0.1'

porta_servidor = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destino = (ip_servidor,porta_servidor)

while True:
    #Mensagem recebera dados do teclado
    mensagem = input()

    udp.sendto(bytes(mensagem,'utf8'), destino)
    #bytes(Mensagem,'urf-8') = converte tipo str para byte