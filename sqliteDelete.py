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

 
sql1=f'DELETE FROM Contato WHERE nome=("{nome}")'

def delete(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)       
    finally:
        print('Registro removido')

delete(vcon,sql1)        
        
        
        
        
vcon.close()        