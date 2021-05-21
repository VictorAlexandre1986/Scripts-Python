from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'CodigoBarras.png','wb') as arquivo:
    EAN13('421466789103', writer=ImageWriter()).write(arquivo)
    
