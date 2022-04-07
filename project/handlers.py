from .crack import bruteforce, brute_freq
from .utils import write_file, analyse_text
from .crypt import encrypt, decrypt
from colorama import Fore, Style
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
    # Check for missing arguments
    if not args.wordlist:
        raise ValueError("No Wordlist Found")
    text = ''
    a_value = ' '.join(args.freq_analysis)
    # Filter letters, numbers and spaces
    text = re.sub(r'[^A-Za-z0-9 ]+', '', a_value)
    # Analyse the frequency
    matches = analyse_text(text, ''.join(args.wordlist))
    avg = float(matches) / len(text.split(' ')) * 100
    if avg > 60:
        print(f'{Fore.GREEN}True with an average of {round(avg, 1)}%{Style.RESET_ALL}')
        return
    print(f'{Fore.YELLOW}False with an average of {round(avg, 1)}%{Style.RESET_ALL}')


def brute_freq_handler(args):
    c_value = ' '.join(args.brute_frequency)
    # Get cipher text
    cipher = open(c_value, 'r').read() if args.sourceFile else c_value
    # Get analysed disctionary
    analyzed = brute_freq(cipher, ''.join(args.wordlist))
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(analyzed, args.output)
    else:
        found = False
        for i in analyzed:
            if analyzed[i] > 60:
                print(f'{Fore.GREEN}{round(analyzed[i], 1)}%{Style.RESET_ALL} : {i}')
                found = True
        if not found:
            print(
                f'{Fore.YELLOW}No Matching Sentences Found For The Given Wordlist{Style.RESET_ALL}')
