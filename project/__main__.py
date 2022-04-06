from .handlers import bruteforce_handler, decrypt_handler, encrypt_handler
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

# -b & --brute
parser.add_argument('-br', '--bruteforce', nargs='+',
                    metavar='PLAIN', help='Cipher text to crack', type=str)

args = parser.parse_args()


def handle_args():
    try:
        # If key isn't in the args,
        if not args.key and (args.encrypt or args.decrypt):
            raise NameError("Key is not defined")
        # If the bruteforce flag used
        elif args.bruteforce:
            bruteforce_handler(args)
        # If the encrypt flag used
        elif args.encrypt:
            encrypt_handler(args)
        # If decrypt flag used,
        elif args.decrypt:
            decrypt_handler(args)
        # If no flags used,
        else:
            raise ValueError("No Arguments given")
    except Exception as e:
        print("Error:", e)