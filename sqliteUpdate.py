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


nome_velho = input('Qual contato deseja atualizar : ')
nome_novo = input('Insira o novo nome')
telefone = input('Insira o novo contato : ')

 
sql1=f'UPDATE Contato SET nome=("{nome_novo}"),celular=("{telefone}") WHERE nome=("{nome_velho}")'

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)       
    finally:
        print('Registro atualizado')

atualizar(vcon,sql1)        
        
        
        
        
vcon.close()        