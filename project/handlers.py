from .crack import bruteforce
from .utils import write_file, analyse_text
from .crypt import encrypt, decrypt
import re


def bruteforce_handler(args):
    c_value = ' '.join(args.bruteforce)
    cracked = []
    if args.sourceFile:
        f = open(c_value, 'r').read()
        cracked = bruteforce(f)
    else:
        cracked = bruteforce(c_value)
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(cracked, args.output)
    else:
        for j in cracked:
            print(j)


def encrypt_handler(args):
    # Extract key as an int from args
    key = int(''.join(map(str, args.key)))
    key *= -1 if args.backwards else 1
    # Get plain text
    e_value = ' '.join(args.encrypt)
    # If source presents,
    # file content will be encrypted
    cipher = ''
    if args.sourceFile:
        f = open(e_value, 'r').read()
        cipher = encrypt(f, key)
    else:
        cipher = encrypt(e_value, key)
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(cipher, args.output)
    else:
        print("Encrypted: " + cipher)


def decrypt_handler(args):
    # Extract key as an int from args
    key = int(''.join(map(str, args.key)))
    key *= -1 if args.backwards else 1
    # Get Cipher text
    d_value = ' '.join(args.decrypt)
    # If source presents,
    # file content will be decrypted
    plain = ''
    if args.sourceFile:
        f = open(d_value, 'r').read()
        plain = decrypt(f, key)
    else:
        plain = decrypt(d_value, key)
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(plain, args.output)
    else:
        print("Decrypted: " + plain)


def freq_analysis_handler(args):
    text = ''
    a_value = ' '.join(args.freq_analysis)
    text = re.sub(r'[^A-Za-z0-9 ]+', '', a_value)
    matches = analyse_text(text, ''.join(args.wordlist))
    l = len(text.split(' '))
    avg = float(matches) / len(text.split(' ')) * 100
    if avg > 80:
        print('True')
    print('False')
