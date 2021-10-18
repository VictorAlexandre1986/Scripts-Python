#pip install python-barcode
#pip install pillow
from barcode import EAN13
from barcode.writer import ImageWriter




codigos_produtos = {
    "Feijão":"553214569874",
    "Arroz" :"123456789101",
    "Macarrao":"564895521455",
    "Azeite"  :"444523669874"
}

for produto in codigos_produtos:
    codigo=codigos_produtos[produto]
    #Precisa de doze digitos
    codigo_barra = EAN13(codigo,writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")
