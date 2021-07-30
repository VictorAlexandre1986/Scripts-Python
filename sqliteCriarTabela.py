import sqlite3
from sqlite3 import Error

def Conexaobanco():
    caminho='Agenda.db'
    conexao = None
    try:
        conexao=sqlite3.connect(caminho)
    except Error as e:
        print(e)
    
    return conexao

vcon=Conexaobanco()

sql='''CREATE TABLE tb_contatos(
    idContato int primary key auto_increment,
    nome varchar(30) not null,
    telefone varchar(20)not null,
    email varchar(20) not null
    );'''

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as e:
        print(e)
        
criarTabela(vcon,sql)

        
        
        
vcon.close()     