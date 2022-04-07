from .crack import bruteforce, brute_freq
from .utils import write_file, analyse_text, get_text
from .crypt import encrypt, decrypt
from colorama import Fore, Style
import re


def bruteforce_handler(args):
    # Get all possibilities of the cipher text
    cracked = bruteforce(get_text(args, 'bruteforce'))
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(cracked, args.output)
    else:
        for j in cracked:
            print(j)


def encrypt_handler(args):
    # Extract key as an int from args
    key = int(''.join(map(str, args.key))) * -1 if args.backwards else 1
    # Get Cipher text
    cipher = encrypt(get_text(args, 'encrypt'), key)
    # Write to the file,
    # If an output path specified
    if args.output:
        write_file(cipher, args.output)
    else:
        print("Encrypted: " + cipher)


def decrypt_handler(args):
    # Extract key as an int from args
    key = int(''.join(map(str, args.key))) * -1 if args.backwards else 1
    # Get plain text
    plain = decrypt(get_text(args, 'decrypt'), key)
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
    # Filter letters, numbers and spaces
    text = re.sub(r'[^A-Za-z0-9 ]+', '', get_text(args, 'freq_analysis'))
    # Analyse the frequency
    matches = analyse_text(text, ''.join(args.wordlist))
    avg = float(matches) / len(text.split(' ')) * 100
    if avg > 60:
        print(f'{Fore.GREEN}True with an average of {round(avg, 1)}%{Style.RESET_ALL}')
        return
    print(f'{Fore.YELLOW}False with an average of {round(avg, 1)}%{Style.RESET_ALL}')


def brute_freq_handler(args):
    # Check for missing arguments
    if not args.wordlist:
        raise ValueError("No Wordlist Found")
    # Get cipher text
    cipher = get_text(args, 'brute_frequency')
    # Get analysed disctionary
    bruteforced = brute_freq(cipher, ''.join(args.wordlist))
    analyzed = bruteforced[0]
    # Write to the file,
    # If an output path specified
    if args.output:
        s = ''
        found = False
        for i in analyzed:
            if analyzed[i] > 60:
                s += f'{round(analyzed[i], 1)}% : {i}\n'
                found = True
        if not found:
            s = f'No Matching Sentences Found For The Given Wordlist'
        write_file(s, args.output)
    else:
        found = False
        for i in analyzed:
            if analyzed[i] > 60:
                print(
                    f'{Fore.GREEN}{round(analyzed[i], 1)}%{Style.RESET_ALL}: {Fore.CYAN}{list(bruteforced[1].keys()).index(i)}{Style.RESET_ALL} : {i}')
                found = True
        if not found:
            print(
                f'{Fore.YELLOW}No Matching Sentences Found For The Given Wordlist{Style.RESET_ALL}')
