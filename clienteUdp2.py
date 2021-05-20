import socket

ip_servidor='127.0.0.1'

porta = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg_envio = input("Digite a mensagem: ......")
    cliente.sendto(msg_envio.encode(),(ip_servidor,porta))
    msg_bytes, ip_servidor = cliente.recvfrom(2048)
    print(msg_bytes.decode())
