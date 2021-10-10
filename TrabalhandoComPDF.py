#pip install pypdf2

import PyPDF2

#Abrindo arquivo dem modo leitura e lendo binario
pdf_file = open('C:\pasta\pdfs','rb')

def ler():
    #Após pegar o binário, pegamos os dados de PDF desse Binario
    dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

    print('Número de paginas : ' + str(dados_do_pdf.numPages))

    #Pegando a pagina 1
    pagina1 = dados_do_pdf.getPage(0)

    #Extraindo o texto da pagina 1
    texto = pagina1.extractText()
    
def merge():
    arq1 = open('C:\pasta\pdfs\relatorio1.pdf','rb')
    arq2 = open('C:\pasta\pdfs\relatorio2.pdf','rb')
    
    dados_do_arq1 = PyPDF2.PdfFileReader(arq1)
    dados_do_arq2 = PyPDF2.PdfFileReader(arq2)
    
    #Declarando um objeto do tipo merge
    merge = PyPDF2.PdfFileMerger()
    
    #Inserindo os pdfs no objeto merge
    merge.append(dados_do_arq1)
    merge.append(dados_do_arq2)
    
    #escrevendo o novo arquivo
    merge.write(f'C:\pasta\pdfs\relatorioFinal.pdf')