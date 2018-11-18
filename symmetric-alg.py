


def main():
    print('[1] Encrypt \n [2] Decrypt')
    choice = raw_input('>')
    print('File Path: ')
    file_path = raw_input ('>')
    print 'Secret Key: '
    key = raw_input ('>')
    # Encrypt
    if choice == "1":
        encrypt (file_path, key)
    # Decrypt
    elif choice == "2":
        decrypt (file_path, key)

    else:
        print 'Invalid Choice'

if __name__ == '__main__':
    main ()