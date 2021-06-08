#Esta classe implementa a rotação de chaves para o Fernet.
#Ele pega uma list de instâncias de Fernet
from cryptography.fernet import Fernet , MultiFernet

key1 = Fernet ( Fernet . generate_key ())
key2 = Fernet ( Fernet . generate_key ())

f = MultiFernet ([ key1 , key2 ])

token = f . encrypt (b'Secret message!')

print(token)

#O multiFernet tenta descriptografar com uma chave de cada vez
#Uma exceção é lançada caso a chave correta não seja encontrada
#A rotação de tokens facilita a substituição de chaves antigas
print(  f . decrypt ( token ))

'''

MultiFernet é  uma prática recomendada e uma maneira de higiene criptográfica
projetada para limitar os danos em caso de um evento não detectado e aumentar
a dificuldade dos ataques
'''

#Criando uma nova chave
key3 = Fernet ( Fernet . generate_key ())

#lista de chaves
f2 = MultiFernet ([ key3 , key1 , key2 ])

#Gira um token criptografando-o
#Se um token foi rotacionado com sucesso, o token rotacionado será retornado.
#Se a rotação falhar, isso gerará uma exceção.
rotated = f2 . rotate ( token )

print(f2 . decrypt ( rotated ))
