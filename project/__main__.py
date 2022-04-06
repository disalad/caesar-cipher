from .crypt import encrypt, decrypt
from .utils import write_file
import argparse

parser = argparse.ArgumentParser(
    description='A tool to Encrypt, Decrypt texts with a substitution cipher given as the key')

# -e & --encrypt
parser.add_argument('-e', '--encrypt', nargs='+',
                    metavar='PLAIN', help='Encrypt the plain text', type=str)
# -d & --decrypt
parser.add_argument('-d', '--decrypt', nargs='+', metavar='CIPHER',
                    help='Decrypt the cipher text', type=str)
# -k & --key
parser.add_argument('-k', '--key', nargs=1, metavar='KEY',
                    help='Represents the number of places for the shift', type=int, default=False)
# -b & --backwards
parser.add_argument('-b', '--backwards', action='store_true')
# -o & --output
parser.add_argument('-o', '--output', nargs=1, type=str,
                    help='Output file directory')
# -s & --source
parser.add_argument('-sf', '--sourceFile', action='store_true')

args = parser.parse_args()


def handle_args():
    # If key isn't in the args,
    if not args.key and (args.encrypt or args.decrypt):
        raise NameError("Key is not defined")
    # If the encrypt flag used
    elif args.encrypt:
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
    # If decrypt flag used,
    elif args.decrypt:
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
    # If no flags used,
    else:
        raise ValueError("No Arguments given")
