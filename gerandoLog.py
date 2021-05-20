import logging
"""
Alguns dados importantes que devem ser inseridos no log:
*data/hora
*Nome do arquivo que gerou o log
*Caminho do arquivo
*Linha do código que gerou o log
*Mensagens padronizadas(sucesso/falha de execução)
*Informações úteis para o usuário

NIVEIS DE LOG
Debug(10):informações detalhadas, normalmente de interesse apenas ao diagnosticar problemas
Info(20):Confirmação de que tudo está funcionando conforme o esperado
Warning(30):Indica de que algo inesperado aconteceu,o software aind está funcionando como esperado
Critical(40):Devido um problema sério, o software não conseguiu executar algumas funções
Error(50):Um erro grave , indicando que i próprio programa pode não conseguir continuar em execução 

"""


#Por padrão log somente acima de 30 que são gravados, na linha abaixo estamos mudando para a partir de nivel 10
logging.basicConfig(filename="teste.log", level=logging.DEBUG)

#Caos tenhamos definido level CRITICAL somente level critical e error serão gravados

def soma(a,b):
    """ Soma a com b"""
    return(a+b)

def subtracao(a,b):
    """ Subtração de a de b"""
    return(a-b)

def multiplicacao(a,b):
    """ Multiplicação de a com b"""
    return(a*b)

def divisao(a,b):
    """ Divisão de a por b"""
    try:
        return (a / b)
    except ZeroDivisionError:
        logging.critical("Não é permitido divisão por zero")
        return


add_resultado = soma(10,2)
logging.info(f'O resultado da soma de 10 com 2 é {add_resultado}')
sub_resultado = subtracao(10,2)
logging.info(f'O resultado da subtração de 10 por 2 é {sub_resultado}')
mul_resultado = multiplicacao(10,2)
logging.info(f'O resultado da multiplicação de 10 por 2 é {mul_resultado}')
div_resultado = divisao(10,0)
logging.info(f'O resultado da divisão de 10 por 2 é {div_resultado}')

