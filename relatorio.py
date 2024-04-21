from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(filename, content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Definindo o conteúdo do relatório
    text = content

    # Escrevendo o texto no PDF
    textobject = c.beginText(50, height - 50)
    textobject.setFont("Helvetica", 12)
    for line in text:
        textobject.textLine(line)
    c.drawText(textobject)

    c.showPage()
    c.save()

# Conteúdo do relatório (exemplo)
report_content = [
    "Relatório de Vendas",
    "-----------------",
    "Produtos vendidos:",
    "1. Produto A - $100",
    "2. Produto B - $150",
    "3. Produto C - $200",
    "",
    "Total de Vendas: $450"
]

# Geração do relatório em PDF
generate_pdf("relatorio.pdf", report_content)

print("Relatório gerado com sucesso!")