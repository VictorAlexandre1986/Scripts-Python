import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

data = (b'a secret message')
aad = (b'authenticated but unencrypted data')

#Uma chave de 256 é gerada
key = AESGCM . generate_key ( bit_length = 256 )

#Criando um objeto AESGCM usando a chave 
aesgcm = AESGCM ( key )

'''O NIST recomenda um comprimento IV de 96 bits para um melhor desempenho,
#mas pode ser de até 2 elevado 64 - 1 bits . NUNCA REJEITE NONCE com uma chave'''
nonce = os . urandom ( 64 )

'''aad : Dados adicionais que devem ser autenticados com a chave,
mas não são criptografados. Pode ser None .'''


ct = aesgcm . encrypt ( nonce , data , aad )


print(aesgcm . decrypt ( nonce , ct , aad ))

#OverflowError - Se data ou data associated_data forem maiores que 2 32 bytes.
