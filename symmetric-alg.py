
def calculate_key(key):
    results = 0
    counter = 0
    # Convert each Character into an INT and added to results
    for char in key:
        counter += 1
        results += ord (char)

    # Return the results divided by the number of Characters in the key
    return int (results / counter)


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