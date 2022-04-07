from .crypt import ALPHEBET, decrypt
from .utils import analyse_text
from operator import itemgetter
import re


def bruteforce(text):
    cracked = []
    # Iterate from 1 to length of the ALPHEBET
    for i in range(1, len(ALPHEBET)):
        cracked.append('Result with key ' + str(i) + ' ' + decrypt(text, i))
    return cracked


def brute_freq(text, wordlist):
    analysed = {}
    decrypted = []
    # Bruteforce and get all possibilities
    for i in range(len(ALPHEBET)):
        decrypted.append(decrypt(text, i))
    # Check whether the given words are present in the given wordlist or not
    for text in decrypted:
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        matches = analyse_text(text, wordlist)
        avg = float(matches) / len(text.split(' ')) * 100
        analysed[text] = avg
    # Sort the analysed texts by average
    analysed = dict(sorted(analysed.items(), key=itemgetter(1), reverse=True))
    return analysed
