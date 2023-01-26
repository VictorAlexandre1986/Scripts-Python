from pydantic import validate_arguments
from typing import Union


#Vai validar os parâmetros da função
@validate_arguments
def multiplicacao(num1: int, num2: int) -> int:
    return num1 * num2


#Vai validar os parâmetros da função , a validação aceitará dois tipos
@validate_arguments
def soma(valor1: Union[int,str], valor2: Union[int,str]):
    return valor1 + valor2


from pydantic.dataclasses import dataclass
#Vai ser feito a conversão de um tipo para outro através do pydantic, no atributo idade em tempo de execução
@dataclass
class Pessoa:
    nome: str
    idade: int


from pydantic import StrictInt
#Não vai aceitar outro valor a não ser o inteiro na idade, não tem casting automático
class Pessoa2:
    nome: str
    idade: StrictInt



from pydantic import BaseModel
#-------------------------Models------------------------------
#Os models do Pydantic são responsáveis pelas validaçõe de dados
#Em um sevidor web
#Validações com pandas
#Validação de configurações

class Cadastro(BaseModel):
    nome: str
    idade: int
    sobrenome: str
    email: str
    senha: str
    ativo: bool = True


# Composição
class Pessoa(BaseModel):
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]


#-------------------Validadores-----------------------
#Validando campos
#Os validadores são divididos em tres grupos
#default:Validaçao durante o carregamento
#pré:Validação antes do carregamento
#por item: Validação de containers(lista-tupla-dicionario)

from pydantic import BaseModel,validator
class Cadastro2(BaseModel):
    email:   str
    senha_1: str
    senha_2: str

    @validator('email')
    def email_deve_ter_arroba(cls, valor):
        #valor passado no load
        if '@' not in valor:
            raise ValueError('Não tem @')
        return valor


    #@validator('*') Verifica se tudo tem mais do que dez caracteres
    @validator('senha_1','senha_2')
    def a_senha_tem_10_caracteres(cls, valor):
        if len(valor)>= 5:
            return valor
        raise ValueError('A senha não tem o minimo de caracteres necessários')

    @validator('senha_2')
    def senha_iguais(cls, valor, values):
        if valor == values['senha_1']:
            return valor
        raise ValueError('Senhas diferentes')


#Pré validação
#O pré validator pode ser usado em chamadas e de transição ou coisas
# que são recebidas em uma forma, mas devem ser processadas de outra
from pydantic import BaseModel, validator

class Pedidos(BaseModel):
    ids: list[int]
# o pre diz que antes do pydantic carrega eu quero modifica os dados
    @validator('ids', pre=True)
    def parse_ids(cls,valor):
        return valor.split(';')


#Validação por item
#Quando lidamos com containers(itens que contém outros itens) podemos validar individualmente cada item
from pydantic import BaseModel, validator

class Pedidos2(BaseModel):
    ids: list[int]

    @validator('ids', each_item=True)
    def parse_ids(cls, valor):
        if valor > 0:
            return valor
        raise ValueError('Id menor que zero')

#Fields
#Além dos campso definidos na linguagem, o Pydantic conta com uma diversidade de campos
#Contrained(PositiveInt,NegativeFloat,...)
#Strict(StrictInt,StrictFloat,...)
#Além das validações tradicionais, o pydantic conta com Fields próprios
#Valida as seguintes opções
#EmailStr - email_validator  -> pip install email_validator
#NameEmail - email_validator
#FilePath
#DirectoryPath
#Cartão de crédito
#Json
#Color
#Urls
#Secrets

from pydantic import BaseModel, EmailStr
class Cadastro3(BaseModel):
    email : EmailStr


#Transformando uma lista de objetos em json em uma lista de objeto python
import string
import json
from pydantic import BaseModel
from pprint import pprint

class User(BaseModel):
    usuario: str | None
    senha : str | None

    @classmethod
    @validator("senha")
    def validar_senha(cls, valor):
        if len(valor)<=10:
            raise ValueError("Senha muito pequena")
        if any(p in valor for p in string.punctuation):
            if any(d in valor for d in string.digits):
                if any(l in valor for l in string.ascii_lowercase):
                    if any(u in valor for u in string.ascii_uppercase):
                        raise ValueError("Usuario inválido")



    @classmethod
    @validator("usuario")
    def usuario_valido(cls,valor):
        if any(p in valor for p in string.ponctuation):
            raise ValueError("Usuario não pode conter pontuação")
        else:
            return valor


if __name__ == "__main__":

    resultado = multiplicacao(2, 5)
    print(resultado)

    resultado = soma("Victor ", "Alexandre")
    print(resultado)

    print(Pessoa(nome="Victor", idade="36"))

    #Convertendo em um objeto python
    print(Cadastro(**{'nome': 'Victor', 'sobrenome':'Braga Ribeiro', 'idade': 36, 'email':'victor.20@gmail.com', 'senha':'123'}))

    pessoa = {
        'nome': 'Victor',
        'idade': 36,
        'sobrenome':'Braga Ribeiro',
        'email':'victor.20@gmail.com',
        'senha':'123'
    }
    print(Cadastro(**pessoa))

    #Composicao
    d = [
         {'nome': 'Victor',  'idade': 36},
         {'nome': 'Xispita', 'idade': 10},
         {'nome': 'Fifi',    'idade': 7},
         {'nome': 'Negona',  'idade': 13}
        ]

    #É feito um casting de um conjunto de dados para um dado único
    print(Pessoas(pessoas=d).pessoas)
    #Repetição mas dentro de um for
    for pessoa in (Pessoas(pessoas=d).pessoas):
        print(pessoa)

    #Cadastro2 Validator
    print(Cadastro2(email='asdas@', senha_1='1234567890', senha_2='1234567890'))


    #Validator
    print(Cadastro2(email='teste@gmail.com', senha_1='1234567890', senha_2='1234567890').json())
    print(Cadastro2(email='teste@gmail.com', senha_1='1234567890', senha_2='1234567890').dict())
    dicionario = {
        'email': 'teste@hotmail.com',
        'senha_1': '01234567890',
        'senha_2': '01234567890'
    }
    x = (Cadastro2(**dicionario).json())
    print(x)


    #Pré validação
    print(Pedidos(ids='1; 2; 3; 4'))

    #Validaçação item por item, se o item for menor que zero retorna erro
    x=Pedidos2(ids=[1, 2, 1, 4, 9])
    print(*x)

    #Criando uma lista de objetos vindo de um arquivo json
    json_users = [User(**pessoa) for pessoa in json.load(open("users.json"))]
    pprint(json_users)

