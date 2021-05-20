import socket

ip_servidor='127.0.0.1'

porta=5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((ip_servidor,porta))

while True:
    msg_bytes, ip_cliente = servidor.recvfrom(2048)
    msg_resposta = msg_bytes.decode().lower()
    servidor.sendto(msg_resposta.encode(), ip_cliente)
    print(msg_resposta)