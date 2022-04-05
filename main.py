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
# -s & --source
parser.add_argument('-s', '--source', action='store_true')

args = parser.parse_args()

ALPHEBET = '0123456789abcdefghijklmnopqrstuvwxyz'


def encrypt(plain_text, key):
    cipher = ''
    # Iterates through the given plain_text
    for i in plain_text:
        # Lower the letter
        lower_i = i.lower()
        # If letter does occur in the ALPHEBET,
        # Encryption will be proceeded
        if lower_i in ALPHEBET:
            ciphered = ''
            # When letter index is higher than 32,
            # Letter can't change position by the KEY
            # So the ciphered letter will be started by the beginning
            if ALPHEBET.find(lower_i) > len(ALPHEBET) - (key + 1):
                ciphered = ALPHEBET[(ALPHEBET.find(
                    lower_i) + key) % len(ALPHEBET)]
            else:
                ciphered = ALPHEBET[ALPHEBET.find(lower_i) + key]
            # If the letter is an uppercase,
            # cipher letter will be uppercased too
            if i.isupper():
                cipher += ciphered.upper()
            else:
                cipher += ciphered
        # If letter doesn't occur in the ALPHEBET,
        # the plain letter will be added to the cipher text
        else:
            cipher += i
    return cipher


def decrypt(cipher_text, key):
    plain = ''
    for i in cipher_text:
        lower_i = i.lower()
        # If letter does occur in the ALPHEBET,
        # Encryption will be proceeded
        if lower_i in ALPHEBET:
            decrypted = ''
            if ALPHEBET.find(lower_i) > len(ALPHEBET) - (key + 1):
                decrypted = ALPHEBET[(ALPHEBET.find(
                    lower_i) - key) % len(ALPHEBET)]
            else:
                decrypted = ALPHEBET[ALPHEBET.find(lower_i) - key]
            # If the letter is an uppercase,
            # decrypted letter will be uppercased too
            if i.isupper():
                plain += decrypted.upper()
            else:
                plain += decrypted
        # If letter doesn't occur in the ALPHEBET,
        # the plain letter will be added to the plain text
        else:
            plain += i
    return plain


if __name__ == "__main__":
    try:
        # If key isn't in the args,
        if not args.key and (args.encrypt or args.decrypt):
            raise NameError("Key is not defined")
        elif args.encrypt:
            # Extract key as an int from args
            key = int(''.join(map(str, args.key)))
            key *= -1 if args.backwards else 1
            # Get plain text
            e_value = ' '.join(args.encrypt)
            # If source presents,
            # file content will be encrypted
            if args.source:
                f = open(e_value, 'r').read()
                print("Encrypted: \n" + encrypt(f, key))
            else:
                print("Encrypted: " + encrypt(e_value, key))
        elif args.decrypt:
            # Extract key as an int from args
            key = int(''.join(map(str, args.key)))
            key *= -1 if args.backwards else 1
            # Get Cipher text
            d_value = ' '.join(args.decrypt)
            # If source presents,
            # file content will be decrypted
            if args.source:
                f = open(d_value, 'r').read()
                print("Decrypted: \n" + decrypt(f, key))
            else:
                print("Decrypted: " + decrypt(d_value, key))
            pass
        else:
            raise ValueError("No Arguments given")
    except Exception as e:
        print("Error:", e)
