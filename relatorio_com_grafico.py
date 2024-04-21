from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

def generate_pdf_with_chart(filename, content, chart_data):
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

    # Adicionando gráfico ao PDF
    chart = VerticalBarChart()
    chart.x = 50
    chart.y = height - 200
    chart.width = 400
    chart.height = 200
    chart.data = [chart_data]
    chart.strokeColor = colors.black
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = max(chart_data) + 10
    chart.categoryAxis.labels.angle = 45

    drawing = Drawing(400, 200)
    drawing.add(chart)
    drawing.drawOn(c, 50, height - 200)

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

# Dados para o gráfico (exemplo)
chart_data = [100, 150, 200]

# Geração do relatório em PDF com gráfico
generate_pdf_with_chart("relatorio_com_grafico.pdf", report_content, chart_data)

print("Relatório com gráfico gerado com sucesso!")
