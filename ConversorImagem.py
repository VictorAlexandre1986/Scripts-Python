from PIL import Image
import os

lista_arquivos = os.listdir("imagens")

for arquivo in lista_arquivos:
    
    imagem = Image.open(f"imagens/{arquivo}").convert("RGB")

    #imagem.save("imagem.jpg")
    
    imagem.save(f'PDF/{arquivo.replace("png","pdf")}')
