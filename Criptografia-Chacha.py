import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

'''
ChaCha20Poly1305 é uma cifra
de fluxo combinada com um MAC que oferece fortes garantias de integridade.
'''

data = (b'a secret message')

#
aad = (b'authenticated but unencrypted data')

#Uma chave de 32 bytes. Isso deve ser mantido em segredo
key = ChaCha20Poly1305 . generate_key ()

#
chacha = ChaCha20Poly1305 ( key )

#nonce = Um valor de 12 bytes. NUNCA REJEITE NONCE com uma chave.
#A reutilização de um nonce com uma determinada key compromete a
#segurança de qualquer mensagem com esse par nonce e key .
nonce = os . urandom ( 12 )

#data = dado a ser criptografado
#aad = Dados adicionais que devem ser autenticados com a chave,
#mas não precisam ser criptografados. Pode ser None .
ct = chacha . encrypt ( nonce , data , aad )

#
print(chacha . decrypt ( nonce , ct , aad ))

#Uma exceção é lançada caso data ou data associated forem maiores que 2 elevado 32 bytes
#OverflowError 
