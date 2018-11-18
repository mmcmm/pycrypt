
def save_file(results, file_path):
    # Create File Object
    f = open (file_path, 'w')
    # Write Results
    f.write (results)
    # Close File Object
    f.close ()


def open_file(file_path):
    # Create File Object
    f = open (file_path, 'r')
    # Read File Contents
    file_contents = f.read ()
    # Close File Object
    f.close ()

    return file_contents

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