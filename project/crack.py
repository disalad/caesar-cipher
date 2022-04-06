from .crypt import ALPHEBET, decrypt

def bruteforce(text):
    cracked = []
    for i in range(1, len(ALPHEBET)):
        cracked.append('Result with key ' + str(i) + ' ' + decrypt(text, i))
    return cracked
