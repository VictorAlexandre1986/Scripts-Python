#pip install pyzbar
#pip install pillow

from pyzbar.pyzbar import decode
from PIL import Image

print(decode(Image.open('qrcode_google.png')))

