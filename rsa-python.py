from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
# from Crypto.Hash import SHA256
import base64

# pip install pycrypto

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"
    
    def __init__(self):
        return

    def __save_file(self, contents, file_name):
        f = open(file_name, 'w')
        f.write(contents)
        f.close()
        
    def __read_file(self, file_name):
        f = open(file_name,'r')
        contents = f.read()
        f.close()
        return contents  

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.exportKey("PEM")
        public_key = keys.publickey().exportKey ("PEM")
        self.__save_file(private_key,self.PRIVATE_KEY_FILE)
        self.__save_file(public_key,self.PUBLIC_KEY_FILE)
        print "Public & Private Keys; generated & saved successfully!"  