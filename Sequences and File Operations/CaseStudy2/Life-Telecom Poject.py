# Build a system where when user enters Reference ID it is encrypted,
# so that hackers cannot view the mapping of Reference ID and finger print

from re import search

Reference_ID = input('Enter Reference_ID:')

# Reference_ID Validation
p = True
while p:
    if len(Reference_ID) == 12:
        break
    elif not search('[a-z]', Reference_ID):
        break
    elif not search('[0-9]', Reference_ID):
        break
    elif not search('[A-Z]', Reference_ID):
        break
    elif not search('[!&%$#@]', Reference_ID):
        break
    else:

        # Encrypting Reference_ID
        cipher_text = ''
        for char in Reference_ID:
            cipher_num = (ord(char)) + 5 % 26
            cipher = chr(cipher_num)
            cipher_text = cipher_text + cipher
        print('\nEncryption:', cipher_text)

        # Decrypting Reference_ID
        decrypt_text = ''
        for char in cipher_text:
            decrypt_num = (ord(char)) - 5 % 26
            decrypt = chr(decrypt_num)
            decrypt_text = (decrypt_text + decrypt)
        print('\nDecryption:', decrypt_text)

        p = False
        break

if p:
    print('Invalid Reference_ID')
