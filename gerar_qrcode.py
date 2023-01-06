#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode


if __name__=='__main__':
    string= "victor"
    url= pyqrcode.create(string)
    url.png("qr.png", scale= 8)