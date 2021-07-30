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


nome = input('Informe seu nome : ')
celular = input('Informe seu numero : ')
 
sql1=f'Insert into Contato (nome,celular) values ("{nome}","{celular}")'
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as e:
        print(e)       

inserir(vcon,sql1)        
        
        
        
        
vcon.close()        