
def save_file(results, file_path):
    f = open(file_path, 'w')
    f.write(results)
    f.close()


def open_file(file_path):
    f = open(file_path, 'r')
    file_contents = f.read()
    f.close()

    return file_contents

def calculate_key(key):
    results = 0
    counter = 0
    for char in key:
        counter += 1
        results += ord(char)

    return int(results / counter)

def encrypt(file_path, key):
    file_contents = open_file(file_path)
    key_calc = calculate_key(key)
    enc_results = ''

    for line in file_contents:
        for wrd in line:
            for char in wrd:
                int_char = ord(char) + key_calc
                enc_results += chr(int_char)

    save_file(enc_results, file_path)
    print '[!] Finished Encryption'

def main():
    print '[1] Encrypt \n [2] Decrypt'
    choice = raw_input('>')
    print 'File Path: '
    file_path = raw_input ('>')
    print 'Secret Key: '
    key = raw_input('>')
   
    if choice == "1":   # Encrypt
        encrypt(file_path, key) 
    elif choice == "2":  # Decrypt
        decrypt(file_path, key)
    else:
        print 'Invalid Choice'

if __name__ == '__main__':
    main ()