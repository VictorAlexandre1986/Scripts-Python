'''
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
data = b"a secret message"
aad = b"authenticated but unencrypted data"
key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
ct = aesgcm.encrypt(nonce, data, aad)
print(ct)
dec=aesgcm.decrypt(nonce, ct, aad)
print(dec)
'''

#https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/#sha-2-family


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"abc")
digest.update(b"123")
x = digest.finalize()

print(x)
