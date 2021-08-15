from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def mp(mm):
    return mm/0.352777

pastaApp = os.path.dirname(__file__)

def criarPDF():
    try:
        cnv = canvas.Canvas(pastaApp+'\\texto2.pdf',pagesize=A4)
        #cnv.drawImage(pastaApp+'\\imagem.jpg',mp(0),mp(247))297 é o máximo altura
        cnv.drawString(mp(100),mp(250),'Victor Alexandre Braga Ribeiro')
        cnv.save()
    except:
        messagebox.showinfo(title='Erro', message='Error ao gerar o pdf')
        return
    messagebox.showinfo(title='Sucesso', message='Arquivo gerado com sucesso')

app=Tk()
app.title('Gerador de pdf')   
app.geometry('600x400') 

btn_criaPDF=Button(app,text='Criar PDF', command=criarPDF)
btn_criaPDF.pack(side='bottom',padx=10)

app.mainloop()





