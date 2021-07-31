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


nome = input('Qual contato está procurando : ')

 
sql1=f'SELECT nome,celular FROM Contato WHERE nome=("{nome}")'

def buscar(conexao,sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado

res = buscar(vcon,sql1)
for r in res:
    print(r)        
        
        
        
        
vcon.close()        