from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64

class AESCrypto:
    
    def md5_hash(self,text):
        h = MD5.new()
        h.update(text)
        return h.hexdigest()
    
        def __init__(self,key):
        self.key = self.md5_hash(key) # 128 bits