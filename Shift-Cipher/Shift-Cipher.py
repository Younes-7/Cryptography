from termcolor import colored, cprint
from pyfiglet import figlet_format

def shift_char(char, key, encrypt=True):
    
    base = ord('A') if char.isupper() else ord('a')
    shift = key if encrypt else -key
    return chr((ord(char) - base + shift) % 26 + base)

def encrypt(plaintext, key=3):
    return ''.join(shift_char(char, key) if char.isalpha() else char for char in plaintext)

def decrypt(ciphertext, key=3):
    return ''.join(shift_char(char, key, encrypt=False) if char.isalpha() else char for char in ciphertext)

def menu():
    print(figlet_format("Younes Khorablou", font="digital"))
    cprint(figlet_format('Shift Cipher'), 'yellow')

    while True:
        choice = input("""\nShift Cipher Encryption & Decryption:
    1: Encrypt a plaintext
    2: Decrypt a ciphertext
    3: Exit
    Choose an option (1, 2, or 3): """)

        if choice == '1':
            plaintext = input("Enter your plaintext for encryption:\n")
            key = int(input("Enter the key for encryption (default is 3 for Caesar):\n"))
            print("Encrypted text:", encrypt(plaintext, key))

        elif choice == '2':
            ciphertext = input("Enter your ciphertext for decryption:\n")
            key = int(input("Enter the key for decryption:\n"))
            print("Decrypted text:", decrypt(ciphertext, key))

        elif choice == '3':
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid option, please choose again.\n")

menu()
