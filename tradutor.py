#pip install translate

from translate import Translator


if __name__=='__main__':
    tradutor= Translator(from_lang="english", to_lang="portuguese")
    traduzido = tradutor.translate("Hello World")
    print(traduzido)

