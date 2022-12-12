from hashlib import sha256

def trasformar_em_hash():
    #Para passar uma informação para sha256 é necessário o dado estar em tipo byte

    #Transformando a string em byte
    nome = b"Victor Alexandre"

    #Outra maneira de transformar uma string em byte é usando o enconde
    sobrenome = "Braga Ribeiro".encode()

    hash = sha256(nome)

    #Mostra em bytes
    print(hash.digest())
    #Mostra em hexadecimal
    print(hash.hexdigest())

if __name__ == "__main__":
    trasformar_em_hash()




