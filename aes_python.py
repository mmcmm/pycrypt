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


    def encrypt(self,cleartext):
        Block_Size = AES.block_size         # Block size - 128 bits
        pad = lambda s: s + (Block_Size - len (s) % Block_Size) * chr (Block_Size - len (s) % Block_Size)
        cleartext_blocks = pad(cleartext)
        
        iv = Random.new().read(Block_Size) # Random IV 
        crypto = AES.new(self.key,AES.MODE_CBC,iv)
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks))    