import hashlib

#Gerando hash de arquivo

caminho = r'CodigoBarras.png'

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()

lista = [md5, sha1, sha256, sha512]


for hash_objeto in lista:
    with open(caminho, 'rb') as file:
        conteudo = file.read()
        hash_objeto.update(conteudo)
        print(f'O hash do {hash_objeto.name} é {hash_objeto.hexdigest()}')
