import bcrypt

#String de bytes
senha = b"Victor"

#hashed = bcrypt.hashpw(senha,bcrypt.gensalt(rounds=14))
hashed = bcrypt.hashpw(senha,bcrypt.gensalt())

if bcrypt.checkpw(senha,hashed):
    print('Senha encontrada')
else:
    print('Senha inválida')

