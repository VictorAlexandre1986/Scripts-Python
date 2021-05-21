import socket

meu_ip='127.0.0.1'

porta=8000

#Sock_stream é tcp
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

meu_servidor = (meu_ip, porta)
#Faz o bind do ip e da porta para começar ouvir
tcp.bind(meu_servidor)

#Começa ouvir
tcp.listen(True)

#pega o ip do cliente que conectou
conexao, docliente = tcp.accept()
print(f'o cliente = {docliente} se conectou')

#Essa variavel vai ser usada para comparar com a variavel da mensagem
testa_msg=''

while True:
    
    
    msg_recebida = conexao.recv(2048)
    
    if msg_recebida != testa_msg:
        print(f'Recebi = {msg_recebida} do cliente {docliente}')


conexao.close()
