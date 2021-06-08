from cryptography.fernet import Fernet

#Criando uma chave
#Uma chave de 32 bytes codificada em base64 
key = Fernet . generate_key ()

print('Chave : ', key)

print('')

f = Fernet ( key )

#O resultado dessa criptografia é conhecido como "token Fernet"
token = f . encrypt (b'Ola mundo!')

print('Criptografada : ',token)

print('')

print('Descriptografada : ',f . decrypt ( token ))

#Retorna o registro de data e hora da criação do token,pode ser usado para expirar
print(f.extract_timestamp(token))


'''
Uma exceção pode ser lançada caso a mensagem a ser criptografada não esteja em bytes
'''
