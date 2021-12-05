import os

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.avi', '.mkv']
imagens_ext = ['.jpg', 'jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf', '.epub']


def pegar_extensao(arquivo):
    index = arquivo.rfind('.')
    return arquivo[index:]


def organizar(diretorio):

    AUDIO_DIR = os.path.join(diretorio, 'audios')
    IMAGEM_DIR = os.path.join(diretorio, 'imagens')
    DOCS_DIR = os.path.join(diretorio, 'documentos')
    VIDEOS_DIR = os.path.join(diretorio, 'videos')
    OUTROS_DIR = os.path.join(diretorio, 'outros')

    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGEM_DIR):
        os.mkdir(IMAGEM_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)


    nomes_arquivos = os.listdir(diretorio)
    nova_pasta=''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in audios_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGEM_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR

            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)

            os.rename(velho, novo)
            print(f'Moveu {velho} para {novo}')

if __name__=='__main__':
    organizar()