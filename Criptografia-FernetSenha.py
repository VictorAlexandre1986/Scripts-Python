import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


password = (b'password')
salt = os . urandom ( 16 )
kdf = PBKDF2HMAC (
   algorithm = hashes . SHA256 (),
   length = 32 ,
   salt = salt ,
   iterations = 100000 ,
   backend = default_backend ()
)
key = base64 . urlsafe_b64encode ( kdf . derive ( password ))
f = Fernet ( key )
token = f . encrypt (b'Secret message!')

print('Criptograda : ',token)
print('')

print('Descriptografada : ',f . decrypt ( token ))
