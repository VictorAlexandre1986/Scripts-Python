import os

audios_ext = ['.mp3','.wav']
videos_ext = ['.mp4','.mov','.avi','.mkv']
imagens_ext = ['.jpg','jpeg','.png','.gif']
documentos_ext = ['.txt','.log','.pdf']

def pegar_extensao(nome):
    indice=nome.rfind('.')
        
def organizar(diretorio):
    
    audio_dir = os.path.join(diretorio,'audios')
    imagem_dir = os.path.join(diretorio,'imagens')
    documento_dir = os.path.join(diretorio,'documentos')
    video_dir = os.path.join(diretorio,'video')
    outros_dir = os.path.join(diretorio,'outros')
    
    if not os.path.isdir(audio_dir):
        os.makedir(audio_dir)
    if not os.path.isdir(imagem_dir):
        os.makedir(imagem_dir)
    if not os.path.isdir(documento_dir):
        os.makedir(documento_dir)
    if not os.path.isdir(video_dir):
        os.makedir(video_dir)
    
    arquivos = os.listdir(diretorio)
    
    nova_pasta=''
    
    for arquivo in arquivos:
        
        if os.path.iffile(os.path.join(diretorio,arquivo)):
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in audios_ext:
                nova_pasta = audio_dir
            elif extensao in videos_ext:
                nova_pasta = video_dir       
            elif extensao in imagens_ext:
                nova_pasta = imagem_dir
            elif extensao in documentos_ext:
                nova_pasta = documento_dir
            else:
                nova_pasta = outros_dir
            
            velho=os.path.join(diretorio,arquivo)
            novo=os.path.join(nova_pasta,arquivo) 
            #movendo arquivos
            os.rename(velho,novo)
            print(f'Moveu {velho} => {novo}')

if __name__=='__main__':
    organizar('downloads')    

